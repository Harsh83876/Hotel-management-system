# CodSoft Python Programming — Week 2 Project
## Hotel Reservation System (Tkinter GUI)

A desktop GUI application for managing a hotel's rooms, guests,
reservations, and billing — built with Python's `tkinter` and `ttk`
widgets, with an admin login gate in front of the dashboard.

---

## 1. Project Overview

A Python-based Hotel Reservation System with a secured admin login,
a sidebar-navigated dashboard, and modules for Room Management,
Guest Management, Reservations, and Billing/Invoice generation —
matching the CodSoft Week 2 project brief.

---

## 2. Features

| Feature                  | Status | Notes |
|---------------------------|--------|-------|
| Admin Login                 | ✅ | Hardcoded credentials (`admin` / `admin123`); wrong credentials show an error dialog |
| Dashboard                    | ✅ | Live counts: Total Rooms, Available, Occupied, Total Guests, Total Reservations, Total Revenue |
| Room Management (Add)          | ✅ | Room Number, Room Type (Standard/Deluxe/Suite dropdown), Price/Night |
| Room Management (View)          | ✅ | Table (Treeview) listing all rooms with status |
| Room Management (Delete)         | ✅ | Select a row in the table, then delete |
| Room Management (Update)          | ⚠️ Not implemented | Only Add/View/Delete are wired up |
| Guest Registration                 | ✅ | Guest ID, Full Name, Phone, Email, Address — all fields required |
| Guest View                          | ✅ | Table listing all registered guests |
| Guest Update / Delete                | ⚠️ Not implemented | Registration and viewing only |
| Room Availability Filtering            | ✅ | The Reservation form's Room ID dropdown only lists rooms currently marked `Available` |
| Reservation Creation                    | ✅ | Booking a room sets that room's status to `Reserved` |
| Reservation List                         | ✅ | Table of all reservations with status |
| Check-In / Check-Out workflow              | ⚠️ Not implemented | Reservations only carry `Reserved` / `Checked-In` labels seeded in sample data; there's no button to transition a reservation between states |
| Billing & Invoice Generation                | ✅ | Select a Reservation ID → generates a formatted invoice: nights × room price + a flat ₹1,000 service charge, plus 12% tax |
| Data Persistence (JSON/CSV)                   | ⚠️ Not implemented | All data (`rooms`, `guests`, `reservations`) lives in in-memory Python lists seeded at startup — **it resets every time the app is restarted** |
| Search / Sort                                    | ⚠️ Not implemented | Not present in the current build |

This is an honest checklist against the full CodSoft brief — the app
is fully functional for the flows it supports (login → book a room →
generate an invoice), but a few bonus items from the spec
(persistence, update/delete for guests, check-in/out state changes,
search & sort) are not yet built.

---

## 3. How It Works

1. **Launch** → Admin Login screen appears (fields are pre-filled with
   the demo credentials `admin` / `admin123` for convenience).
2. **Login** → lands on the **Dashboard**, which summarizes the hotel's
   current in-memory state.
3. **Rooms** tab → add a new room (ID, type, price) or delete an
   existing one from the table.
4. **Guests** tab → register a new guest; all five fields are
   required.
5. **Reservations** tab → pick a Guest ID and an *available* Room ID,
   enter check-in/check-out dates (`YYYY-MM-DD`), and book. The room
   immediately flips to `Reserved` and drops out of the availability
   dropdown.
6. **Billing** tab → pick a Reservation ID and click **Generate
   Bill** to produce a formatted invoice in the text panel.

### Sample data pre-loaded at startup

**Rooms**

| Room ID | Type     | Price/Night | Status    |
|---------|----------|-------------|-----------|
| 101     | Standard | ₹1,800      | Available |
| 205     | Deluxe   | ₹3,500      | Occupied  |
| 301     | Suite    | ₹6,000      | Available |

**Guests**

| Guest ID | Name         | Phone       | Email             | Address   |
|----------|--------------|-------------|-------------------|-----------|
| G1025    | Alex Johnson | 9812345678  | alex@email.com    | New Delhi |
| G1026    | Priya Sharma | 9887654321  | priya@email.com   | Mumbai    |

**Reservations**

| Res. ID | Guest | Room | Check-In   | Check-Out  | Status      |
|---------|-------|------|------------|------------|-------------|
| R5001   | G1025 | 205  | 2026-08-25 | 2026-08-28 | Checked-In  |

---

## 4. Billing Formula

```
Room Charges     = nights × room price-per-night
Service Charges  = ₹1,000 (flat, fixed in code)
Subtotal         = Room Charges + Service Charges
Tax (12%)        = Subtotal × 0.12
TOTAL            = Subtotal + Tax
```

Example from the walkthrough below (Reservation `R5007`, Suite room
`301` at ₹6,000/night, 9 nights, 2026-09-11 → 2026-09-20):

```
Room Charges     : ₹54,000.00
Service Charges  : ₹1,000.00
Subtotal         : ₹55,000.00
Tax (12%)        : ₹6,600.00
TOTAL AMOUNT     : ₹61,600.00
```

---

## 5. Installation & Running

Requires **Python 3.8+** with `tkinter` (bundled with the standard
Windows/macOS installers; on Linux install with
`sudo apt install python3-tk` if missing). No external pip
dependencies are needed.

```bash
python main.py
```

Log in with:
- **Username:** `admin`
- **Password:** `admin123`

---

## 6. Project Structure

```
submission/
├── main.py             # Full application source (single file)
├── README.md            # This file
└── screenshots/          # Application screenshots (see below)
```

---

## 7. Screenshots

| # | Screenshot | Description |
|---|------------|--------------|
| 1 | `01_admin_login.jpg` | Admin login screen |
| 2 | `02_dashboard.jpg` | Dashboard after login, showing live metric cards |
| 3 | `03_guest_management_form_filled.jpg` | Guest Management — registration form filled in for a new guest (Harsh) |
| 4 | `04_guest_management_registered.jpg` | Guest Management — table updated after registering the new guest |
| 5 | `05_reservation_booking_form.jpg` | Reservations — booking form filled in for a new reservation (R5007) |
| 6 | `06_reservation_list.jpg` | Reservations — table showing both reservations after booking |
| 7 | `07_billing_select_reservation.jpg` | Billing — Reservation ID dropdown open |
| 8 | `08_billing_invoice_generated.jpg` | Billing — generated invoice for reservation R5007 |

---

## 8. Known Limitations / Suggested Next Steps

- **No persistence** — add JSON (or CSV) load/save so rooms, guests,
  and reservations survive a restart.
- **No Update for Rooms/Guests** — only Add + Delete are wired up;
  Update handlers could reuse the existing form fields.
- **No Check-In/Check-Out actions** — reservations are created as
  `Reserved` but nothing in the UI moves them to `Checked-In` /
  `Checked-Out`, and room status doesn't get freed up on checkout.
- **No overlap/duplicate-booking validation** — a room already
  `Reserved` simply won't appear in the availability dropdown, but
  there's no explicit date-overlap check if IDs are typed by hand.
- **Service charge is hardcoded** (`₹1,000`) rather than user-entered
  per booking.
- **No search/sort controls** on the Rooms or Guests tables yet.

None of the above block the current submission from running or
demonstrating the core flow end-to-end — they're natural next
iterations if more time is available before the deadline.

---

*Built with Passion • Coded with Purpose — CodSoft Python Programming, Week 2*
