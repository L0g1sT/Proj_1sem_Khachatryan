import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="../PZ_16/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить товар', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="../PZ_16/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="../PZ_16/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить товар", command=self.delete_records, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="../PZ_16/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск товара", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="../PZ_16/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('sname_m', 'sname_c', 'name_cl', 'value', 'sell_t',), height=20, show='headings')

        self.tree.column('sname_m', width=100, anchor=tk.CENTER)
        self.tree.column('sname_c', width=180, anchor=tk.CENTER)
        self.tree.column('name_cl', width=160, anchor=tk.CENTER)
        self.tree.column('value', width=140, anchor=tk.CENTER)
        self.tree.column('sell_t', width=200, anchor=tk.CENTER)

        self.tree.heading('sname_m', text='ФИО клиента')
        self.tree.heading('sname_c', text='ФИО мастера')
        self.tree.heading('name_cl', text='Тип чистки')
        self.tree.heading('value', text='Стоимость')
        self.tree.heading('sell_t', text='Скидка')

        self.tree.pack()

    def records(self, sname_m, sname_c, name_cl, value, sell_t):
        self.db.insert_data(sname_m, sname_c, name_cl, value, sell_t)
        self.view_records()

    def update_record(self, sname_m, sname_c, name_cl, value, sell_t):
        self.db.cur.execute("""UPDATE base SET sname_m=?, sname_c=?, name_cl=?, value=?, sell_t=?, WHERE value=?""",
                            (sname_m, sname_c, name_cl, value, sell_t, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM base""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM base WHERE sname_m=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_name_t(self, user_id):
        user_id = ("%" + user_id + "%",)
        self.db.cur.execute("""SELECT * FROM base WHERE value LIKE ?""", user_id)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить товар')
        self.geometry('600x270+600+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='ФИО мастера')
        label_description.place(x=50, y=25)
        self.entry_des = ttk.Entry(self)
        self.entry_des.place(x=220, y=25)

        label_name = tk.Label(self, text='ФИО клиента')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=220, y=50)

        label_name1 = tk.Label(self, text='Тип чистки')
        label_name1.place(x=50, y=75)
        self.entry1_name = ttk.Entry(self)
        self.entry1_name.place(x=220, y=75)

        label_old = tk.Label(self, text='Стоимость')
        label_old.place(x=50, y=100)
        self.entry_z = ttk.Entry(self)
        self.entry_z.place(x=220, y=100)

        label_score = tk.Label(self, text='Скидка')
        label_score.place(x=50, y=125)
        self.entry_c = ttk.Entry(self)
        self.entry_c.place(x=220, y=125)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=220)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_des.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry1_name.get(),
                                                                       self.entry_z.get(),
                                                                       self.entry_c.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_des.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry1_name.get(),
                                                                          self.entry_z.get(),
                                                                          self.entry_c.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("400x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск по Стоимости")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=175, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_name_t(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('../PZ_16/ob.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS base (
                sname_m TEXT NOT NULL,
                sname_c TEXT NOT NULL,
                name_cl TEXT NOT NULL,
                value INTEGER NOT NULL,
                sell_t INTEGER
                )""")

    def insert_data(self, sname_m, sname_c, name_cl, value, sell_t):
        self.cur.execute("""INSERT INTO base(sname_m, sname_c, name_cl, value, sell_t) VALUES (?, ?, ?, ?, ?)""",
                             (sname_m, sname_c, name_cl, value, sell_t))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Химчистка")
    root.geometry("1050x450+300+200")
    root.resizable(False, False)
    root.mainloop()
