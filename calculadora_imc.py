import tkinter as tk


def calculadora_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "usted tiene bajo peso."
    elif 18.5 <= imc < 24.9:
        categoria = "usted está dentro de los valores normales."
    elif 25 <= imc < 29.9:
        categoria = "usted tiene sobrepeso. Considere ver un profesional."
    elif imc >= 30:
        categoria = "usted tiene obesidad. Considere ver un profesional."
    
    return f"Su IMC es {imc:.2f}, {categoria}"

def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        resultado = calculadora_imc(peso, altura)
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, ingrese valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("400x300") 
ventana.configure(bg="#F9F8F7")

fuente = ("Arial", 14)

tk.Label(ventana, text="Ingrese su peso en Kgs:", bg="#F9F8F7", font=fuente, fg="#2A2D3A").pack(pady=10)
entry_peso = tk.Entry(ventana, font=fuente)
entry_peso.pack(pady=5)

tk.Label(ventana, text="Ingrese su altura en Mts:", bg="#F9F8F7", font=fuente, fg="#2A2D3A").pack(pady=10)
entry_altura = tk.Entry(ventana, font=fuente)
entry_altura.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular, bg="#C47769", fg="white", font=fuente)
boton_calcular.pack(pady=20)

label_resultado = tk.Label(ventana, text="", bg="#F9F8F7", font=fuente, fg="#2A2D3A")
label_resultado.pack(pady=10)

ventana.mainloop()
