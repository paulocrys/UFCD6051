import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Necessário instalar: pip install Pillow

def criar_portfolio():
    root = tk.Tk()
    root.title("Portfólio do Estudante")
    root.geometry("500x600")
    root.configure(bg="#f0f0f0")

    # --- Dados do Estudante ---
    dados = {
        "nome": "Paulo Martins",
        "idade": "43 anos",
        "email": "paulo.martins.a@hotmail.com",
        "Curso": "Técnico Instalações Elétricas",
        "ufcds": [
            "UFCD 6051 - Programação - Algoritmia",
            "UFCD 6029 - Técnologia e montagem de circuitos eletrónicos",
        ]
    }

    # --- Secção da Foto ---
    # Nota: Substitui 'foto.jpg' pelo caminho real da tua imagem
    try:
        img = Image.open(r"C:\Users\DELL\Documents\trabalho_entregar\Imagem.jpeg")
        img = img.resize((150, 200), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(img)
        lbl_foto = tk.Label(root, image=foto, bg="#f0f0f0")
        lbl_foto.image = foto # Manter referência
        lbl_foto.pack(pady=20)
    except:
        lbl_placeholder = tk.Label(root, text="[Foto não encontrada]", bg="#ccc", width=20, height=10)
        lbl_placeholder.pack(pady=20)

    # --- Informações Pessoais ---
    tk.Label(root, text=dados["nome"], font=("Arial", 16, "bold"), bg="#f0f0f0").pack()
    tk.Label(root, text=f"Idade: {dados['idade']}", font=("Arial", 11), bg="#f0f0f0").pack()
    tk.Label(root, text=f"Email: {dados['email']}", font=("Arial", 11), bg="#f0f0f0").pack()
    tk.Label(root, text=dados["Curso"], font=("Arial", 11, "italic"), fg="#555", bg="#f0f0f0").pack()

    # --- Lista de UFCDs ---
    tk.Label(root, text="UFCDs:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(20, 5))
    
    frame_lista = tk.Frame(root, bg="white", padx=10, pady=10, relief="groove", borderwidth=1)
    frame_lista.pack(padx=20, fill="both", expand=True)

    for ufcd in dados["ufcds"]:
        lbl_item = tk.Label(frame_lista, text=f"• {ufcd}", bg="white", font=("Arial", 10), anchor="w")
        lbl_item.pack(fill="x")

    root.mainloop()

if __name__ == "__main__":
    criar_portfolio()

