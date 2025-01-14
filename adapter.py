import socket
import xmlrpc.client

# Konfiguracja serwera Socket
PORT = 2221
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Tworzenie serwera Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Konfiguracja klienta XML-RPC
server_url = "http://127.0.0.1:2223"
client = xmlrpc.client.ServerProxy(server_url)


# Funkcja przetwarzająca wiadomość i komunikująca się z serwerem XML-RPC
def process_message(message):
    try:
        # Parsowanie wiadomości od klienta
        message = message.strip()
        parts = message.split(";")
        jaka_funkcja = parts[0]
        imie = parts[1] if len(parts) > 1 else None
        numer = parts[2] if len(parts) > 2 else None

        # Łączenie z serwerem RPC
        server_rpc = xmlrpc.client.ServerProxy("http://127.0.0.1:2223")

        if jaka_funkcja == "1":  # Dodanie kontaktu
            print(f"[PROCESS_MESSAGE] Dodawanie kontaktu: {imie}, {numer}")
            response = server_rpc.zapisz_abonenta(imie, numer)
            print(f"[RPC RESPONSE] {response}")
            return response  # Odpowiedź RPC jest przekazywana bez zmian

        elif jaka_funkcja == "2":  # Pobranie książki telefonicznej
            print("[PROCESS_MESSAGE] Pobieranie książki telefonicznej")
            response = server_rpc.pobierz_ksiazke()
            print(f"[RPC RESPONSE] {response}")
            return response  # Odpowiedź RPC jest przekazywana bez zmian

        else:
            print("[PROCESS_MESSAGE] Nieznana funkcja")
            return "Błędne żądanie"
    except Exception as e:
        print(f"[ERROR] Błąd w process_message: {e}")
        return "Błąd komunikacji z serwerem AppBack-rpc"

# Funkcja obsługująca klienta Socket
def q_for_func(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    try:
        while connected:
            data = conn.recv(2048)
            if not data:
                break
            message = data.decode(FORMAT).strip()
            print(f"[{addr}] Received message: {message}")

            # Przetwarzanie wiadomości i wywołanie funkcji RPC
            response = process_message(message)

            # Dodanie zakończenia "CR/LF/CR/LF" do odpowiedzi
            response_with_end = f"{response} CR/LF/CR/LF"

            # Wysłanie odpowiedzi do klienta
            print(f"[ADAPTER] Sending response to client: {response_with_end}")
            conn.send(response_with_end.encode(FORMAT))

            # Obsługa rozłączenia
            if message.startswith("3"):
                connected = False
    except ConnectionResetError as e:
        print(f"[ERROR] Connection with {addr} lost unexpectedly: {e}")
    finally:
        conn.close()
        print(f"[CONNECTION CLOSED] {addr} disconnected.")


# Funkcja uruchamiająca serwer
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        try:
            conn, addr = server.accept()
            q_for_func(conn, addr)
        except Exception as e:
            print(f"[ERROR] Problem z obsługą klienta: {e}")


if __name__ == "__main__":
    print("[STARTING] Adapter is starting...")
    start()
