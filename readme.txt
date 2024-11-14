Aplikacja służy do automatycznego konwertowania treści artykułu z pliku tekstowego na kod HTML z odpowiednią strukturą. Artykuł jest przetwarzany przez model OpenAI, który generuje kod HTML zawierający:

Odpowiednie tagi HTML do strukturyzacji treści.
Miejsca na grafiki oznaczone tagiem <img> z placeholderem dla źródła obrazu oraz atrybutami alt z opisem promptu do generowania obrazu.
Podpisy pod grafikami umieszczone w tagach <figcaption>.
Gotowy plik HTML jest zapisany do pliku i może być wykorzystany do tworzenia stron internetowych na podstawie zawartości tekstowej.

Wymagania
Python 3.6 lub nowszy
Biblioteka OpenAI (openai)
Konto OpenAI z ważnym kluczem API
Instalacja
Sklonuj repozytorium:

git clone https://github.com/twoj_uzytkownik/nazwa_repozytorium.git
cd nazwa_repozytorium
Zainstaluj bibliotekę OpenAI:

pip install openai
Ustaw zmienną środowiskową OPENAI_API_KEY:

Uzyskaj klucz API z OpenAI (https://platform.openai.com).
Ustaw klucz jako zmienną środowiskową:
Linux/Mac: export OPENAI_API_KEY="twoj_klucz_api"
Windows: set OPENAI_API_KEY="twoj_klucz_api"
Użycie
Umieść plik z artykułem tekstowym w katalogu projektu. Domyślnie skrypt oczekuje pliku o nazwie article.txt, ale można zmienić nazwę pliku w kodzie.

Uruchom skrypt:

python app.py
Skrypt automatycznie wykona następujące kroki:

Wczyta treść artykułu z pliku (article.txt).
Prześle treść artykułu do API OpenAI w celu wygenerowania HTML.
Zapisze wygenerowany kod HTML do pliku artykul.html.
Wynik: Plik artykul.html zawiera wygenerowany HTML, który możesz otworzyć w przeglądarce lub umieścić na stronie internetowej.

Funkcjonalności
load_article(filepath)
Funkcja load_article wczytuje treść artykułu z pliku tekstowego i zwraca go jako tekst. Przyjmuje jako argument filepath, czyli ścieżkę do pliku artykułu.

generate_html_from_article(article_content)
Funkcja generate_html_from_article korzysta z API OpenAI, aby przekształcić zawartość tekstową artykułu na kod HTML. HTML zawiera:

Tagi strukturyzujące (nagłówki, akapity, itp.).
Miejsca na obrazy z tagiem <img src="image_placeholder.jpg" alt="description">.
Podpisy pod obrazami umieszczone w tagach <figcaption>.
save_html_to_file(html_content, filename="artykul.html")
Funkcja save_html_to_file zapisuje wygenerowany kod HTML do pliku. Domyślnie zapisuje jako artykul.html, ale można zmienić nazwę pliku, przekazując inny argument filename.

W repozytorium został przygotowany szablon do strony html. Jeżeli chcesz zobaczyć wynik przygotowanego artykułu z zastosowanymi stylami, które są zaproponowane przez twórce, zawartość z pliku artykul.html należy wkleić do sekcji body w pliku podglad.html.


Problemy i rozwiązania
Błąd autoryzacji: Upewnij się, że zmienna środowiskowa OPENAI_API_KEY jest poprawnie ustawiona. Sprawdź, czy masz aktywne połączenie internetowe i prawidłowy klucz API.
Nieprawidłowy format HTML: Upewnij się, że treść artykułu jest dobrze sformatowana, aby model mógł odpowiednio zinterpretować zawartość. Zbyt długi artykuł może być skrócony przez model – rozważ podział tekstu na mniejsze części.