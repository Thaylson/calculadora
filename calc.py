import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")

        self.frame = ctk.CTkFrame(self, width=400, height= 50)
        self.frame.pack()
        self.lb_title = ctk.CTkLabel(self.frame, 
                                    text="Calculadora",
                                    font=('Arial', 30),
                                    corner_radius=2)
        self.lb_title.pack(pady=10)

        self.entry = ctk.CTkEntry(self, width=300, font=('Comic Sans',20))
        self.entry.pack(pady=10)

        self.result = ctk.CTkLabel(self, text="", text_color="white", font=('Comic Sans',24,'bold'))
        self.result.pack(pady=10)


        # Adicionando botões de números
        self.create_number_buttons()
        # Adicionando botões de operações
        self.create_operator_buttons()

    def create_number_buttons(self):
        numbers_frame = ctk.CTkFrame(self)
        numbers_frame.pack()

        numbers = '7894561230'
        row, col = 0, 0
        for num in numbers:
            btn = ctk.CTkButton(numbers_frame, 
                                fg_color= ('gray'),
                                hover_color= 'darkorange',
                                text=num, 
                                width=65, 
                                height=65, 
                                command=lambda n=num: self.add_to_entry(n), 
                                font=('Comic Sans', 24),
                                corner_radius=2)
            btn.grid(row=row, 
                    column=col,
                    padx=20,
                    pady=10)
            
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Botão () (Parênteses)
        btn_parentheses = ctk.CTkButton(numbers_frame, 
                                        text='()',
                                        fg_color='gray',
                                        hover_color='darkorange',
                                        width=65, 
                                        height=65,
                                        font=('Comic Sans',24),
                                        corner_radius=2,
                                        command=self.toggle_parentheses)
        btn_parentheses.grid(row=row, 
                            column=1, 
                            padx=10, 
                            pady=5)
        
        btn_clear = ctk.CTkButton(numbers_frame, 
                            text='C', 
                            text_color='red',
                            fg_color='gray',
                            hover_color='darkorange',
                            width=65, 
                            height=65,
                            font=('Comic Sans',24, 'bold'),
                            corner_radius=2,
                            command=self.clear_all)
        btn_clear.grid(row=row, 
                    column=2, 
                    padx=10, 
                    pady=5)
        



    def create_operator_buttons(self):
        operators_frame = ctk.CTkFrame(self)
        operators_frame.pack()

        operators = ['+', '-', '*', '/']
        row, col = 0, 0
        for op in operators:
            btn = ctk.CTkButton(operators_frame,
                                text=op, 
                                fg_color='darkorange',
                                hover_color= 'gray',
                                width=50, 
                                height=50, 
                                command=lambda o=op: self.add_to_entry(o),
                                font=('Comic Sans', 24),
                                corner_radius=2)
            btn.grid(row=row, 
                    column=col,
                    padx=10, 
                    pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Botão de igual
        btn_equal = ctk.CTkButton(operators_frame, 
                                  text='=', 
                                  text_color= 'black',
                                  fg_color='darkgreen',
                                  hover_color= 'lightgray',
                                  width=50, 
                                  height=50,
                                  font=('Comic Sans',24),
                                  corner_radius=2,
                                  command=self.calcular)
        btn_equal.grid(row=row, 
                       column=5, 
                       columnspan=2, 
                       padx=10, 
                       pady=5)

    def clear_all(self):
        self.entry.delete(0, ctk.END)  # Limpa a entrada
        self.result.configure(text="")  # Limpa o resultado

    def toggle_parentheses(self):
        current_text = self.entry.get()
        open_count = current_text.count('(')
        close_count = current_text.count(')')
        
        # Verifica se há um parêntese aberto não fechado
        if open_count > close_count:
            self.entry.insert(ctk.END, ')')
        else:
            self.entry.insert(ctk.END, '(')
        
    def add_to_entry(self, value):
        self.entry.insert(ctk.END, value)

    def calcular(self):
        try:
            resultado = eval(self.entry.get())
            self.result.configure(text=str(resultado))
        except Exception as e:
            self.result.configure(text="Erro: " + str(e))


#app
app = App()
app.geometry("400x550")
app.title("Calculadora")
app.resizable(True,True)
app.mainloop()
