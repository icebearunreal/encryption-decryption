import sys,platform
try:import tkinter as tk;from tkinter import messagebox;from tkinter import ttk
except ImportError:
 e="It looks like 'tkinter'...";messagebox.showerror("Tkinter Not Found",e);sys.exit(1)

def make_it_secret(txt,m):
 k=["qwertyuiop","asdfghjkl","zxcvbnm"];r=[]
 for c in txt:
  l=c.lower();f=False
  for row in k:
   if l in row:
    i=row.find(l)
    if m=="encrypt":
     s=row[0] if i==len(row)-1 else row[i+1]
    elif m=="decrypt":
     s=row[-1] if i==0 else row[i-1]
    r.append(s.upper()if c.isupper()else s);f=True;break
  if not f:r.append(c)
 return"".join(r)

def handle_encryption():
 m=input_text_widget.get(1.0,tk.END).strip()
 if not m:messagebox.showwarning("Input Error","Enter text to encrypt.");return
 e=make_it_secret(m,"encrypt")
 output_text_widget.config(state=tk.NORMAL);output_text_widget.delete(1.0,tk.END)
 output_text_widget.insert(tk.END,e);output_text_widget.config(state=tk.DISABLED)

def handle_decryption():
 m=input_text_widget.get(1.0,tk.END).strip()
 if not m:messagebox.showwarning("Input Error","Enter text to decrypt.");return
 d=make_it_secret(m,"decrypt")
 output_text_widget.config(state=tk.NORMAL);output_text_widget.delete(1.0,tk.END)
 output_text_widget.insert(tk.END,d);output_text_widget.config(state=tk.DISABLED)

def copy_result():
 r=output_text_widget.get(1.0,tk.END).strip()
 if r:root.clipboard_clear();root.clipboard_append(r);messagebox.showinfo("Copied!","Result copied to clipboard.")
 else:messagebox.showinfo("Nothing to Copy","There's no result to copy yet.")

root=tk.Tk();root.title("Secret Tool 🤫 💀💀💀💀");root.geometry("600x600");root.resizable(False,False)
root.configure(bg="#1e1e2f")  # Dark background

s=ttk.Style();s.theme_use('clam')
s.configure('TFrame',background='#1e1e2f');s.configure('TLabel',background='#1e1e2f',foreground='white',font=('Helvetica',12))
s.configure('TButton',font=('Helvetica',10,'bold'),padding=8,background='#444',foreground='white')
s.map('TButton',background=[('active','#888')],foreground=[('pressed','black')])

f=ttk.Frame(root,padding="20 20 20 20");f.pack(fill=tk.BOTH,expand=True)

i_lbl=ttk.Label(f,text="Enter your message:");i_lbl.pack(pady=(10,5))
input_text_widget=tk.Text(f,height=7,width=60,wrap=tk.WORD,bd=2,relief=tk.FLAT,font=('TkFixedFont',11),bg='#2e2e3f',fg='#e6e6e6',insertbackground='white');input_text_widget.pack(pady=5)
input_text_widget.bind("<FocusIn>",lambda e:input_text_widget.config(relief=tk.RIDGE))
input_text_widget.bind("<FocusOut>",lambda e:input_text_widget.config(relief=tk.FLAT))

b_f=ttk.Frame(f);b_f.pack(pady=15)
ttk.Button(b_f,text="Encrypt",command=handle_encryption).pack(side=tk.LEFT,padx=10)
ttk.Button(b_f,text="Decrypt",command=handle_decryption).pack(side=tk.RIGHT,padx=10)

o_lbl=ttk.Label(f,text="Result:");o_lbl.pack(pady=(10,5))
output_text_widget=tk.Text(f,height=7,width=60,wrap=tk.WORD,state=tk.DISABLED,bd=2,relief=tk.FLAT,font=('TkFixedFont',11),bg='#2e2e3f',fg='#e6e6e6');output_text_widget.pack(pady=5)
output_text_widget.bind("<FocusIn>",lambda e:output_text_widget.config(relief=tk.RIDGE))
output_text_widget.bind("<FocusOut>",lambda e:output_text_widget.config(relief=tk.FLAT))

ttk.Button(f,text="📋 Copy Result",command=copy_result).pack(pady=10)

root.mainloop()
