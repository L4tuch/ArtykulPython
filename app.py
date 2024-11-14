import os
import openai

def load_article(filepath):
    """Wczytuje treść artykułu z pliku tekstowego."""
    with open(filepath, 'r', encoding='utf-8') as file:
        article_content = file.read()
    return article_content


def generate_html_from_article(article_content):
    """Przekazuje treść artykułu do OpenAI w celu wygenerowania HTML."""
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Odczyt klucza API ze zmiennej środowiskowej
    
    prompt = f"""
    Przekształć poniższą całą treść artykułu na kod HTML, który będzie miał, dpowiednie tagi HTML do strukturyzacji treści, miejsca na grafiki oznaczone tagiem <img> z atrybutem src="image_placeholder.jpg", każde <img> musi mieć atrybut alt z opisem promptu do wygenerowania obrazu. Umieść podpisy pod grafikami używając odpowiedniego tagu HTML - figcaption. Zwrócona treść powinna zawierać jedynie zawartość pomiędzy tagami <body> i </body> zatem nie dołączaj znaczników <html>, <head> ani <body>. sam tekst z odpowiednimi znacznikami dla danej części artykułu. 

    Treść artykułu:
    {article_content}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an HTML generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.5,
    )

    html_content = response['choices'][0]['message']['content'].strip()
    return html_content  # Zwraca wygenerowany HTML


def save_html_to_file(html_content, filename="artykul.html"):
    """Zapisuje wygenerowany HTML do pliku."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Główna część aplikacji
if __name__ == "__main__":
    # Ścieżka do pliku z artykułem
    article_path = 'article.txt'  
    # Wczytaj artykuł
    article_content = load_article(article_path)
    # Wygeneruj HTML
    html_content = generate_html_from_article(article_content)
    # Zapisz HTML do pliku
    save_html_to_file(html_content)
