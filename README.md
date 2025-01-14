# Python-Adapter-Studies
Adapter XML-RPC Socket
Ten projekt przedstawia adapter napisany w Pythonie, który integruje komunikację pomiędzy serwerem opartym na socketach a serwerem XML-RPC. Projekt został stworzony w ramach pracy semestralnej i ma na celu pokazanie umiejętności integracji różnych technologii w jednym systemie.

Opis
Adapter działa jako pośrednik, który:

Odbiera wiadomości od klientów za pomocą protokołu socket.
Przetwarza wiadomości, wykonując odpowiednie operacje.
Komunikuje się z serwerem XML-RPC, aby wykonać żądane akcje.
Wysyła odpowiedzi z serwera XML-RPC z powrotem do klienta socket.
Główne funkcjonalności
Dodawanie kontaktu: Przesyłanie danych kontaktowych (imię i numer) do serwera XML-RPC.
Pobieranie książki telefonicznej: Otrzymywanie pełnej listy kontaktów z serwera XML-RPC.
Zarządzanie połączeniem: Obsługa klienta socket, w tym przetwarzanie wiadomości i zamykanie połączenia.
Wymagania
Aby uruchomić ten projekt, potrzebujesz:

Python 3.8+.
Zainstalowanego pakietu xmlrpc.client (wbudowanego w Python).
Działającego serwera XML-RPC na porcie 2223.
Upewnij się, że serwer XML-RPC działa pod adresem http://127.0.0.1:2223.
Adapter zacznie nasłuchiwać na porcie 2221.

Struktura komunikacji
Wiadomości przesyłane do adaptera powinny mieć określony format:
<funkcja>;<imię>;<numer>
funkcja:
1: Dodanie kontaktu.
2: Pobranie książki telefonicznej.
3: Rozłączenie.
Przykłady:

1;Jan;123456789 – Dodanie kontaktu Jan z numerem 123456789.
2; – Pobranie książki telefonicznej.
Odpowiedź od serwera jest zakończona ciągiem CR/LF/CR/LF.

Obsługa błędów
W przypadku problemów z połączeniem lub przetwarzaniem wiadomości adapter zwróci odpowiednie komunikaty diagnostyczne na konsolę, np.:

[ERROR] Problem z obsługą klienta.
[ERROR] Błąd w process_message.
Licencja
Ten projekt jest dostępny na licencji MIT. Szczegóły znajdziesz w pliku LICENSE.

Kontakt
Jeśli masz pytania dotyczące tego projektu, skontaktuj się ze mną poprzez salalomon@gmail.com
lub odwiedź mój profil GitHub.

ENG

Python-Adapter-Studies
XML-RPC Socket Adapter

This project showcases an adapter written in Python that integrates communication between a socket-based server and an XML-RPC server. The project was developed as part of a semester assignment and aims to demonstrate the ability to integrate different technologies into a single system.

Description
The adapter acts as an intermediary that:

Receives messages from clients using the socket protocol.
Processes the messages and performs appropriate operations.
Communicates with the XML-RPC server to execute the requested actions.
Sends responses from the XML-RPC server back to the socket client.
Key Features
Adding a Contact: Sends contact data (name and number) to the XML-RPC server.
Retrieving the Phonebook: Fetches the complete contact list from the XML-RPC server.
Connection Management: Handles socket client connections, including message processing and disconnection.
Requirements
To run this project, you need:

Python 3.8+.
The xmlrpc.client package (built into Python).
A running XML-RPC server on port 2223.
Make sure the XML-RPC server is running at http://127.0.0.1:2223.
The adapter will listen on port 2221.

Communication Structure
Messages sent to the adapter should follow this specific format:
<function>;<name>;<number>
function:
1: Add a contact.
2: Retrieve the phonebook.
3: Disconnect.
Examples:

1;John;123456789 – Adds a contact named John with the number 123456789.
2; – Retrieves the phonebook.
The response from the server is terminated with CR/LF/CR/LF.

Error Handling
In case of connection issues or message processing errors, the adapter will return appropriate diagnostic messages to the console, such as:

[ERROR] Problem with client handling.
[ERROR] Error in process_message.
License
This project is available under the MIT License. See the LICENSE file for details.

Contact
If you have any questions about this project, feel free to contact me at salalomon@gmail.com
or visit my GitHub profile.
