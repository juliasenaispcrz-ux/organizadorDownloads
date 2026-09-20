import os
import shutil
from pathlib import Path

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores e Executaveis": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Musicas": [".mp3", ".wav", ".flac", ".ogg"]
}

def organizar_downloads():
    caminho_downloads = Path.home() / "Downloads"
    
    if not caminho_downloads.exists():
        print(f"Erro: A pasta {caminho_downloads} nao foi encontrada.")
        return

    print(f"Organizando arquivos em: {caminho_downloads}\n")
    arquivos_movidos = 0

    for item in caminho_downloads.iterdir():
        if item.is_dir() or item.name == "organizador.py":
            continue
            
        extensao = item.suffix.lower()
        pasta_destino = "Outros"  

        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                pasta_destino = categoria
                break

        caminho_destino = caminho_downloads / pasta_destino
        caminho_destino.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(item), str(caminho_destino / item.name))
            print(f"[SUCESSO] Movido: '{item.name}' -> '{pasta_destino}/'")
            arquivos_movidos += 1
        except Exception as e:
            print(f"[ERRO] Nao foi possivel mover '{item.name}': {e}")

    print(f"\nConcluido! {arquivos_movidos} arquivos foram organizados com sucesso.")

if __name__ == "__main__":
    organizar_downloads()
