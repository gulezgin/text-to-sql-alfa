from text_to_sql import TextToSQL

def main():
    converter = TextToSQL()
    
    print("Text-to-SQL Dönüştürücüye Hoş Geldiniz!")
    print("Çıkmak için 'q' yazın")
    print("\nÖrnek sorgular:")
    print("- müşteriler tablosundan göster")
    print("- siparişler tablosundan şartıyla siparis_id eşittir 123")
    print("- ürünler tablosundan şartıyla fiyat büyüktür 100")
    
    while True:
        text = input("\nLütfen bir sorgu yazın: ")
        
        if text.lower() == 'q':
            print("Program sonlandırılıyor...")
            break
            
        try:
            sql = converter.convert_to_sql(text)
            print("\nOluşturulan SQL sorgusu:")
            print(sql)
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    main()