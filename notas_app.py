import os
ARCHIVO_NOTAS = "mis_notas.txt"

def cargar_notas():
  notas = []
  if os.path.exists(ARCHIVO_NOTAS):
    with open(ARCHIVO_NOTAS, 'r', encoding='utf-8') as archivo:
      contenido = archivo.read().strip()
      if contenido:
        notas = contenido.split("---")
  return notas

def guardar_notas(lista_de_notas):
  """Toma una lista de notas y las guarda en el archivo."""
  with open(ARCHIVO_NOTAS, 'w', encoding='utf-8') as archivo:
    archivo.write("---".join(lista_de_notas))

def mostrar_menu():
  """Muestra las opciones disponibles."""
  print("\n" + "="*40)
  print("       📓 BLOC DE NOTAS VICO v1.0")
  print("="*40)

def main():
  """Funcion principal que controla el flujo del programa."""
  print("Bienvenida a tu block de notas personal!")
  notas = cargar_notas()

  while True:
    mostrar_menu()
    opcion = input("\n👉 Selecciona una opción (1-5): ").strip()

    if opcion == "1":
        print("\n[Crear nueva nota]")
        print("Escribe tu nota. Presiona Enter dos veces para terminar.")
        lineas = []
        while True:
          linea = input()
          if linea == "":
             break
          lineas.append(linea)
        from datetime import datetime
        hora_actual = datetime.now().strftime("%H:%M")
        nueva_nota = f"[{hora_actual}] " + "\n".join(lineas)
        if nueva_nota:
           notas.append(nueva_nota)
           guardar_notas(notas)
           print("✅ Nota guardada correctamente.")
        else:
           print("❌ La nota está vacía. No se guardó.")

    elif opcion == "2":
        print(f"\n[Lista de notas - Total: {len(notas)}]")
      if not notas:
        print("No hay notas guardadas.")
      else:
        for i, nota in enumerate(notas, 1):
          vista_previa = (nota[:50] + "...") if len(nota) > 50 else nota
        print(f"{i}. {vista_previa.replace(chr(10), ' ')}")

    elif opcion == "3":
        print("\n[Leer una nota]")
  if not notas:
        print("No hay notas para leer.")
    else:
      try:
        num = int(input(f"¿Qué número de nota quieres leer? (1 a {len(notas)}): "))
        if 1 <= num <= len(notas):
            print(f"\n📄 NOTA #{num}:")
            print("-"*30)
            print(notas[num-1])
            print("-"*30)
        else:
            print(f"❌ Número inválido. Debe ser entre 1 y {len(notas)}.")
      except ValueError:
        print("❌ Por favor, ingresa un número válido")

    elif opcion == "4":
        print("\n[Eliminar una nota]")
    if not notas:
           print("No hay notas para eliminar.")
       else:
           try:
              num = int(input(f"¿Qué número de nota quieres eliminar? (1 a {len(notas)}): "))
              if 1 <= num <= len(notas):
                  nota_eliminada = notas.pop(num-1)
                  guardar_notas(notas)
                  print(f"✅ Nota #{num} eliminada.")
              else:
                  print(f"❌ Número inválido.")
           except ValueError:
              print("❌ Por favor, ingresar un número válido.")

    elif opcion == "5":
       guardar_notas(notas)
       print("\n💾 Notas guardadas. ¡Hasta pronto, Vico!")
       break

  else:
       print("❌ Opción no válida. Por favor elige 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
  main()
      
