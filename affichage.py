# -*- coding: utf-8 -*-
import tkinter as tk
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import filedialog, scrolledtext
import os
# Scrap les élement selectionnées et les enregistre dans un fichier JSON
def scrap():
    data = {
    "url": url.get(),
    "cookie": cookie.get(),
    }
    texte = text.get("1.0", "end-1c")
    liste = texte.split(", ") 
    driver = webdriver.Chrome()
    driver.get(url.get())
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    clickable = driver.find_elements(By.XPATH, cookie.get())
    print(cookie.get())
    if clickable:
        action = ActionChains(driver)
        action.click(clickable[0])
        action.perform()
    else:
        print("Impossible de trouver le cookie")
    val = 0
    for i in liste:
        try:
            elem = driver.find_elements(By.CLASS_NAME, i)
            data[f"valeur_{val}"] = []
            for e in elem:
                if e.text != "":
                    data[f"valeur_{val}"].append(e.text)
            val += 1
        except:
            print(f"Erreur lors de la récupération de la classe {i}")
    now = datetime.now()
    date_str = now.strftime("%m-%d-%Hh%Mm")
    nom_fichier = f"./data/data_{date_str}.json"
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(data, fichier, indent=4, ensure_ascii=False)
        

# Afficher le fichier JSON
def display_json_file():
    file_path = file_entry.get()
    if file_path:
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
            formatted_json = json.dumps(data, indent=2, ensure_ascii=False)
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.INSERT, formatted_json)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.INSERT, f"Erreur : {e}")
    else:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.INSERT, "Veuillez sélectionner un fichier JSON.")

# Sélectionner le fichier JSON
def select_json_file():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    file_entry.config(state="normal")
    text_area.pack(padx=10, pady=10)
    save_button.pack()
    delete_button.pack()
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")],initialdir=data_dir)
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
    display_json_file()

# Modifier le fichier JSON
def save_json_file():
    file_path = file_entry.get()
    try:
        data = json.loads(text_area.get("1.0", tk.END))
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Contenu JSON invalide.")

# Supprimer le fichier JSON 
def delete_json_file():
    file_path = file_entry.get()
    if os.path.exists(file_path):
        # Supprimer le fichier
        os.remove(file_path)
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.INSERT, f"Le fichier {file_path} a été supprimé avec succès.")
    else:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.INSERT, f"Le fichier {file_path} n'existe pas.")

# Initialise la fenetre tkinter
root = tk.Tk()
root.iconbitmap("scrappi.ico")
root.title("Scrappi")
root.geometry("750x600")
root.resizable(True, True)

# Début de la fenetre tkinter
label = tk.Label(root, text="Entrez Url du site :")
label.pack(pady=1,)

url = tk.Entry(root, width=50)
url.pack()

label = tk.Label(root, text="Xpath cookie:")
label.pack(pady=1)

cookie = tk.Entry(root, width=50)
cookie.pack()

label = tk.Label(root, text="Class a scrap :")
label.pack(pady=1)

text = tk.Text(root, height=5, width=50)
text.pack()

bouton = tk.Button(root, text="Valider", command=scrap)
bouton.pack(pady=3)

label = tk.Label(root, text="Contenue Json :")
label.pack(pady=3)

file_entry = tk.Entry(root, width=50, state="readonly")
file_entry.pack(pady=10)

select_button = tk.Button(root, text="Sélectionner un fichier JSON", command=select_json_file)
select_button.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=80, height=10,font=("DejaVu Sans Mono", 12))
text_area.pack_forget()

save_button = tk.Button(root, text="Enregistrer", command=save_json_file)
save_button.pack_forget()

delete_button = tk.Button(root, text="Supprimer", command=delete_json_file)
delete_button.pack_forget()

# Fin de la fenetre tkinter
root.mainloop()