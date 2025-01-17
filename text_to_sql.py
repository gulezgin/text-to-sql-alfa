import re
from typing import Dict, List

class TextToSQL:
    def __init__(self):
        self.keywords = {
            "göster": "SELECT",
            "bul": "SELECT",
            "listele": "SELECT",
            "nereden": "FROM",
            "tablosundan": "FROM",
            "şartıyla": "WHERE",
            "koşuluyla": "WHERE",
            "sırala": "ORDER BY",
            "grupla": "GROUP BY"
        }
        
        self.tables = {
            "müşteriler": "customers",
            "siparişler": "orders",
            "ürünler": "products"
        }

    def convert_to_sql(self, text: str) -> str:
        text = text.lower()
        query_parts: Dict[str, str] = {
            "SELECT": "*",
            "FROM": "",
            "WHERE": "",
            "ORDER BY": "",
            "GROUP BY": ""
        }

        # Temel dönüşümleri yap
        for tr_keyword, sql_keyword in self.keywords.items():
            if tr_keyword in text:
                # FROM kısmını işle
                if sql_keyword == "FROM":
                    for tr_table, eng_table in self.tables.items():
                        if tr_table in text:
                            query_parts[sql_keyword] = eng_table
                            break
                
                # WHERE kısmını işle
                elif sql_keyword == "WHERE":
                    where_pattern = f"{tr_keyword}\s+(.*?)\s+(eşittir|büyüktür|küçüktür)\s+(.*?)(?:\s|$)"
                    where_match = re.search(where_pattern, text)
                    if where_match:
                        field, operator, value = where_match.groups()
                        operator_map = {
                            "eşittir": "=",
                            "büyüktür": ">",
                            "küçüktür": "<"
                        }
                        query_parts[sql_keyword] = f"{field} {operator_map[operator]} '{value}'"

        # SQL sorgusunu oluştur
        sql_parts = []
        for key, value in query_parts.items():
            if value:
                sql_parts.append(f"{key} {value}")
        
        return " ".join(sql_parts)