# main.py
def mensagem_acolhimento():
    print("🌷 Olá! Às vezes a dor só precisa ser ouvida.")
    print("Hoje, só por hoje, respire fundo e se cuide com leveza.")
    print("Você não precisa provar nada. 💖")

def enviar_pdf():
    print("\n📩 Enviando seu presente com frases para acalmar a alma...")
    print("➡️print("➡️ Link para download do PDF: https://drive.google.com/file/d/1Z4_tmXtOEqoqDoi_zm1XStPhy-7Vdg5f/view?usp=sharing")

def redirecionar_whatsapp():
    numero = "5541991557569"  # Substitua com seu número real com DDD, sem + ou traços
    link = f"https://wa.me/{numero}?text=Oi+Simone,+vi+seu+bot+e+quero+falar+com+você"
    print("\n💬 Redirecionando para atendimento direto com Simone:")
    print(f"➡️ {link}")

# Execução do bot
mensagem_acolhimento()
enviar_pdf()
redirecionar_whatsapp()
