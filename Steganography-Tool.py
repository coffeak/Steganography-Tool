import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import stepic
import base64
import os


def select_file(entry_widget):
    """Open file dialog to select a file"""
    file_path = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)


def ask_save_location(extension):
    """Ask user for the output file location, automatically suggesting the correct file format"""
    return filedialog.asksaveasfilename(defaultextension=extension,
                                        filetypes=[(f"{extension.upper()} Files", f"*{extension}"), ("All Files", "*.*")])


def embed_data():
    """Embed secret data into an image"""
    image_path = entry_image.get()
    secret_path = entry_secret.get()

    if not image_path or not secret_path:
        messagebox.showwarning("Warning", "Please select all required files!")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    if not output_path:
        messagebox.showwarning("Warning", "No output file selected!")
        return

    try:
        with open(secret_path, "rb") as secret_file:
            secret_data = secret_file.read()

        # Get the original file extension
        file_extension = os.path.splitext(secret_path)[1]

        # Encode secret data and append file extension at the beginning
        encoded_secret = base64.b64encode(file_extension.encode() + b"::" + secret_data).decode()

        image = Image.open(image_path)

        # Convert image to RGB if needed
        if image.mode not in ("RGB", "RGBA", "CMYK"):
            image = image.convert("RGB")

        encoded_image = stepic.encode(image, encoded_secret.encode())
        encoded_image.save(output_path, "PNG")
        messagebox.showinfo("Success", "Secret data successfully embedded!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def extract_data():
    """Extract hidden data from an image"""
    image_path = entry_extract_image.get()

    if not image_path:
        messagebox.showwarning("Warning", "Please select an image file!")
        return

    try:
        image = Image.open(image_path)

        # Convert image to RGB if needed
        if image.mode not in ("RGB", "RGBA", "CMYK"):
            image = image.convert("RGB")

        extracted_data = stepic.decode(image)

        # Decode Base64 data
        decoded_data = base64.b64decode(extracted_data)

        # Extract file extension and actual data
        split_data = decoded_data.split(b"::", 1)
        if len(split_data) != 2:
            raise ValueError("Invalid hidden data format.")

        file_extension = split_data[0].decode()
        actual_data = split_data[1]

        # Ask user for save location with correct extension
        output_path = ask_save_location(file_extension)
        if not output_path:
            messagebox.showwarning("Warning", "No output file selected!")
            return

        with open(output_path, "wb") as output_file:
            output_file.write(actual_data)

        messagebox.showinfo("Success", "Secret data successfully extracted!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# GUI Setup
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("500x450")

# Embedding Section
tk.Label(root, text="Embed Data", font=("Arial", 12, "bold")).pack(pady=5)

frame_embed = tk.Frame(root)
frame_embed.pack(pady=5)

entry_image = tk.Entry(frame_embed, width=40)
entry_image.pack(side=tk.LEFT)
tk.Button(frame_embed, text="Browse", command=lambda: select_file(entry_image)).pack(side=tk.LEFT)

tk.Label(root, text="Secret File:").pack()
frame_secret = tk.Frame(root)
frame_secret.pack(pady=5)

entry_secret = tk.Entry(frame_secret, width=40)
entry_secret.pack(side=tk.LEFT)
tk.Button(frame_secret, text="Browse", command=lambda: select_file(entry_secret)).pack(side=tk.LEFT)

tk.Button(root, text="Embed Data", command=embed_data, bg="lightblue").pack(pady=10)

# Extraction Section
tk.Label(root, text="Extract Data", font=("Arial", 12, "bold")).pack(pady=5)

frame_extract = tk.Frame(root)
frame_extract.pack(pady=5)

entry_extract_image = tk.Entry(frame_extract, width=40)
entry_extract_image.pack(side=tk.LEFT)
tk.Button(frame_extract, text="Browse", command=lambda: select_file(entry_extract_image)).pack(side=tk.LEFT)

tk.Button(root, text="Extract Data", command=extract_data, bg="lightgreen").pack(pady=10)

# Developer Info
tk.Label(root, text="Developed by www.coffeak.com", font=("Arial", 10, "italic")).pack(pady=10)

root.mainloop()
