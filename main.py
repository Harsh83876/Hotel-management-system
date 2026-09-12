import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ComprehensiveHotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft Hotel Management System - Admin Login")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f4f6f9")

        # In-memory database lists
        self.rooms = [
            {"id": "101", "type": "Standard", "price": 1800, "status": "Available"},
            {"id": "205", "type": "Deluxe", "price": 3500, "status": "Occupied"},
            {"id": "301", "type": "Suite", "price": 6000, "status": "Available"}
        ]
        
        self.guests = [
            {"id": "G1025", "name": "Alex Johnson", "phone": "9812345678", "email": "alex@email.com", "address": "New Delhi"},
            {"id": "G1026", "name": "Priya Sharma", "phone": "9887654321", "email": "priya@email.com", "address": "Mumbai"}
        ]

        self.reservations = [
            {"res_id": "R5001", "guest_id": "G1025", "room_id": "205", "in_date": "2026-08-25", "out_date": "2026-08-28", "status": "Checked-In"}
        ]

        # Main Layout Container
        self.container = tk.Frame(self.root, bg="#f4f6f9")
        self.container.pack(fill="both", expand=True)

        self.show_login_screen()

    def show_login_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        login_frame = tk.Frame(self.container, bg="#1e293b")
        login_frame.pack(fill="both", expand=True)

        center_card = tk.Frame(login_frame, bg="#0f172a", bd=2, relief="solid")
        center_card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=360)

        tk.Label(center_card, text="ADMIN LOGIN", bg="#0f172a", fg="white", font=("Arial", 16, "bold")).pack(pady=(30, 5))
        tk.Label(center_card, text="Hotel Reservation System", bg="#0f172a", fg="#94a3b8", font=("Arial", 10)).pack(pady=(0, 20))

        form_sub = tk.Frame(center_card, bg="#0f172a")
        form_sub.pack(padx=30, fill="x")

        tk.Label(form_sub, text="Username:", bg="#0f172a", fg="white", font=("Arial", 10)).pack(anchor="w", pady=(0, 5))
        e_user = tk.Entry(form_sub, font=("Arial", 11))
        e_user.pack(fill="x", pady=(0, 15))
        e_user.insert(0, "admin")

        tk.Label(form_sub, text="Password:", bg="#0f172a", fg="white", font=("Arial", 10)).pack(anchor="w", pady=(0, 5))
        e_pass = tk.Entry(form_sub, show="*", font=("Arial", 11))
        e_pass.pack(fill="x", pady=(0, 20))
        e_pass.insert(0, "admin123")

        def handle_login():
            if e_user.get() == "admin" and e_pass.get() == "admin123":
                self.show_main_app()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!")

        tk.Button(center_card, text="Login", bg="#0ea5e9", fg="white", font=("Arial", 11, "bold"),
                  bd=0, padx=20, pady=8, activebackground="#0284c7", activeforeground="white",
                  command=handle_login).pack(fill="x", padx=30)

    def show_main_app(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        # Sidebar Navigation
        self.sidebar = tk.Frame(self.container, bg="#1e293b", width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Main Content Area
        self.main_content = tk.Frame(self.container, bg="#f4f6f9")
        self.main_content.pack(side="right", expand=True, fill="both")

        self.setup_sidebar()
        self.load_module("Dashboard")

    def setup_sidebar(self):
        tk.Label(self.sidebar, text="HOTEL ADMIN", bg="#1e293b", fg="white", font=("Arial", 16, "bold")).pack(pady=20)

        nav_items = ["Dashboard", "Rooms", "Guests", "Reservations", "Billing", "Logout"]
        for item in nav_items:
            tk.Button(self.sidebar, text=item, bg="#1e293b", fg="white", activebackground="#334155", 
                      activeforeground="white", bd=0, anchor="w", padx=20, pady=12, font=("Arial", 11),
                      command=lambda n=item: self.load_module(n)).pack(fill="x")

    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def load_module(self, name):
        if name == "Logout":
            self.show_login_screen()
            return

        if name == "Dashboard":
            self.render_dashboard()
        elif name == "Rooms":
            self.render_rooms_module()
        elif name == "Guests":
            self.render_guests_module()
        elif name == "Reservations":
            self.render_reservations_module()
        elif name == "Billing":
            self.render_billing_module()

    # --- 1. DASHBOARD ---
    def render_dashboard(self):
        self.clear_content()
        tk.Label(self.main_content, text="Hotel Management Dashboard", bg="#f4f6f9", fg="#1e293b", font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=20)

        cards_frame = tk.Frame(self.main_content, bg="#f4f6f9")
        cards_frame.pack(fill="x", padx=20)

        total_rooms = len(self.rooms)
        avail_rooms = len([r for r in self.rooms if r["status"] == "Available"])
        occ_rooms = total_rooms - avail_rooms
        total_guests = len(self.guests)
        total_res = len(self.reservations)

        metrics = [
            ("Total Rooms", str(total_rooms)),
            ("Available Rooms", str(avail_rooms)),
            ("Occupied Rooms", str(occ_rooms)),
            ("Total Guests", str(total_guests)),
            ("Total Reservations", str(total_res)),
            ("Total Revenue", "₹12,880")
        ]

        for i, (title, val) in enumerate(metrics):
            card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", width=160, height=85)
            card.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
            card.pack_propagate(False)

            tk.Label(card, text=title, bg="white", fg="#64748b", font=("Arial", 9)).pack(anchor="w", padx=10, pady=(10, 0))
            tk.Label(card, text=val, bg="white", fg="#1e293b", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=(5, 10))

    # --- 2. ROOMS MODULE (CRUD) ---
    def render_rooms_module(self):
        self.clear_content()
        tk.Label(self.main_content, text="Room Management (CRUD)", bg="#f4f6f9", fg="#1e293b", font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=20)

        form_frame = tk.Frame(self.main_content, bg="white", bd=1, relief="solid")
        form_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(form_frame, text="Room Number:", bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        e_id = tk.Entry(form_frame, font=("Arial", 10))
        e_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Room Type:", bg="white", font=("Arial", 10)).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        c_type = ttk.Combobox(form_frame, values=["Standard", "Deluxe", "Suite"], state="readonly", font=("Arial", 10))
        c_type.grid(row=0, column=3, padx=10, pady=10)
        c_type.current(0)

        tk.Label(form_frame, text="Price/Night (₹):", bg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        e_price = tk.Entry(form_frame, font=("Arial", 10))
        e_price.grid(row=1, column=1, padx=10, pady=10)

        def add_room():
            rid, rtype, rprice = e_id.get(), c_type.get(), e_price.get()
            if not rid or not rprice:
                messagebox.showerror("Error", "All fields are required!")
                return
            self.rooms.append({"id": rid, "type": rtype, "price": float(rprice), "status": "Available"})
            messagebox.showinfo("Success", "Room added successfully!")
            self.render_rooms_module()

        tk.Button(form_frame, text="Add Room", bg="#10b981", fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5, command=add_room).grid(row=1, column=3, padx=10, pady=10)

        columns = ("Room ID", "Type", "Price Per Night", "Status")
        tree = ttk.Treeview(self.main_content, columns=columns, show="headings", height=8)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for r in self.rooms:
            tree.insert("", "end", values=(r["id"], r["type"], f"₹{r['price']}", r["status"]))
        tree.pack(padx=20, pady=10, fill="x")

        def delete_room():
            selected = tree.selection()
            if not selected:
                messagebox.showerror("Error", "Select a room to delete")
                return
            val = tree.item(selected, "values")
            self.rooms = [r for r in self.rooms if r["id"] != val[0]]
            self.render_rooms_module()

        tk.Button(self.main_content, text="Delete Selected Room", bg="#ef4444", fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5, command=delete_room).pack(anchor="w", padx=20)

    # --- 3. GUESTS MODULE ---
    def render_guests_module(self):
        self.clear_content()
        tk.Label(self.main_content, text="Guest Management", bg="#f4f6f9", fg="#1e293b", font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=20)

        form_frame = tk.Frame(self.main_content, bg="white", bd=1, relief="solid")
        form_frame.pack(padx=20, pady=10, fill="x")

        fields = ["Guest ID", "Full Name", "Phone", "Email", "Address"]
        entries = {}
        for i, field in enumerate(fields):
            tk.Label(form_frame, text=field + ":", bg="white", font=("Arial", 9)).grid(row=i//2, column=(i%2)*2, padx=10, pady=8, sticky="w")
            ent = tk.Entry(form_frame, font=("Arial", 10), width=20)
            ent.grid(row=i//2, column=(i%2)*2+1, padx=10, pady=8)
            entries[field] = ent

        def add_guest():
            data = {k: v.get() for k, v in entries.items()}
            if not all(data.values()):
                messagebox.showerror("Error", "All fields are required!")
                return
            self.guests.append({"id": data["Guest ID"], "name": data["Full Name"], "phone": data["Phone"], "email": data["Email"], "address": data["Address"]})
            messagebox.showinfo("Success", "Guest registered successfully!")
            self.render_guests_module()

        tk.Button(form_frame, text="Register Guest", bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5, command=add_guest).grid(row=3, column=3, padx=10, pady=10)

        columns = ("Guest ID", "Full Name", "Phone", "Email", "Address")
        tree = ttk.Treeview(self.main_content, columns=columns, show="headings", height=6)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140)

        for g in self.guests:
            tree.insert("", "end", values=(g["id"], g["name"], g["phone"], g["email"], g["address"]))
        tree.pack(padx=20, pady=10, fill="x")

    # --- 4. RESERVATIONS MODULE ---
    def render_reservations_module(self):
        self.clear_content()
        tk.Label(self.main_content, text="Reservation & Booking Management", bg="#f4f6f9", fg="#1e293b", font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=20)

        form_frame = tk.Frame(self.main_content, bg="white", bd=1, relief="solid")
        form_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(form_frame, text="Res ID:", bg="white", font=("Arial", 9)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        e_resid = tk.Entry(form_frame, font=("Arial", 10), width=15)
        e_resid.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Guest ID:", bg="white", font=("Arial", 9)).grid(row=0, column=2, padx=10, pady=8, sticky="w")
        c_guest = ttk.Combobox(form_frame, values=[g["id"] for g in self.guests], state="readonly", font=("Arial", 10), width=12)
        c_guest.grid(row=0, column=3, padx=10, pady=8)

        tk.Label(form_frame, text="Room ID:", bg="white", font=("Arial", 9)).grid(row=0, column=4, padx=10, pady=8, sticky="w")
        c_room = ttk.Combobox(form_frame, values=[r["id"] for r in self.rooms if r["status"] == "Available"], state="readonly", font=("Arial", 10), width=12)
        c_room.grid(row=0, column=5, padx=10, pady=8)

        tk.Label(form_frame, text="Check-In (YYYY-MM-DD):", bg="white", font=("Arial", 9)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
        e_in = tk.Entry(form_frame, font=("Arial", 10), width=15)
        e_in.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Check-Out (YYYY-MM-DD):", bg="white", font=("Arial", 9)).grid(row=1, column=2, padx=10, pady=8, sticky="w")
        e_out = tk.Entry(form_frame, font=("Arial", 10), width=15)
        e_out.grid(row=1, column=3, padx=10, pady=8)

        def make_reservation():
            resid, gid, rid, ind, outd = e_resid.get(), c_guest.get(), c_room.get(), e_in.get(), e_out.get()
            if not resid or not gid or not rid or not ind or not outd:
                messagebox.showerror("Error", "All fields are required!")
                return
            
            self.reservations.append({"res_id": resid, "guest_id": gid, "room_id": rid, "in_date": ind, "out_date": outd, "status": "Reserved"})
            for r in self.rooms:
                if r["id"] == rid:
                    r["status"] = "Reserved"
            messagebox.showinfo("Success", "Reservation created successfully!")
            self.render_reservations_module()

        tk.Button(form_frame, text="Book Room", bg="#10b981", fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5, command=make_reservation).grid(row=1, column=5, padx=10, pady=8)

        columns = ("Reservation ID", "Guest ID", "Room ID", "Check-In", "Check-Out", "Status")
        tree = ttk.Treeview(self.main_content, columns=columns, show="headings", height=6)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130)

        for res in self.reservations:
            tree.insert("", "end", values=(res["res_id"], res["guest_id"], res["room_id"], res["in_date"], res["out_date"], res["status"]))
        tree.pack(padx=20, pady=10, fill="x")

    # --- 5. BILLING MODULE ---
    def render_billing_module(self):
        self.clear_content()
        tk.Label(self.main_content, text="Billing & Invoice Generation", bg="#f4f6f9", fg="#1e293b", font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=20)

        form_frame = tk.Frame(self.main_content, bg="white", bd=1, relief="solid")
        form_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(form_frame, text="Select Reservation ID:", bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=15, pady=15, sticky="w")
        c_res = ttk.Combobox(form_frame, values=[res["res_id"] for res in self.reservations], state="readonly", font=("Arial", 10))
        c_res.grid(row=0, column=1, padx=15, pady=15)

        bill_output = tk.Text(self.main_content, height=12, width=65, font=("Courier", 10))
        bill_output.pack(padx=20, pady=10)

        def generate_bill():
            selected_rid = c_res.get()
            if not selected_rid:
                messagebox.showerror("Error", "Please select a reservation ID!")
                return
            
            res = next((r for r in self.reservations if r["res_id"] == selected_rid), None)
            room = next((rm for rm in self.rooms if rm["id"] == res["room_id"]), None)

            if not res or not room:
                messagebox.showerror("Error", "Record not found!")
                return

            d1 = datetime.strptime(res["in_date"], "%Y-%m-%d")
            d2 = datetime.strptime(res["out_date"], "%Y-%m-%d")
            nights = max((d2 - d1).days, 1)

            room_charges = nights * room["price"]
            service_charges = 1000
            subtotal = room_charges + service_charges
            tax = subtotal * 0.12  # 12% tax as per project specs
            total = subtotal + tax

            bill_text = f"""
==================================================
                 HOTEL COMFORT STAY INVOICE
==================================================
 Reservation ID  : {res['res_id']}
 Guest ID        : {res['guest_id']}
 Room Number     : {res['room_id']} ({room['type']})
 Duration        : {nights} Nights ({res['in_date']} to {res['out_date']})
--------------------------------------------------
 Room Charges    : ₹{room_charges:,.2f}
 Service Charges : ₹{service_charges:,.2f}
--------------------------------------------------
 Subtotal        : ₹{subtotal:,.2f}
 Tax (12%)       : ₹{tax:,.2f}
==================================================
 TOTAL AMOUNT    : ₹{total:,.2f}
==================================================
"""
            bill_output.delete("1.0", tk.END)
            bill_output.insert(tk.END, bill_text)

        tk.Button(form_frame, text="Generate Bill", bg="#10b981", fg="white", font=("Arial", 10, "bold"), bd=0, padx=20, pady=8, command=generate_bill).grid(row=0, column=2, padx=15, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = ComprehensiveHotelApp(root)
    root.mainloop()
