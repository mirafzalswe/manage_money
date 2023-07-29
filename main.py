from database import Database
from config import user, database, host, password

def check_balance():
    card_id = int(input('Kartangizni raqamini kiriting: '))
    balance = db.get_balance(card_id)
    if balance is not None:
        print(f"Sizning balansigizda {balance} pul bor")
    else:
        print("Karta notog'ri kiritlgan! ")


def send_money():
    name_to = input("Kimga pul otkazmoxchisiz: ")
    summ = int(input("Otkazmoxchi bolgan summani kiritng: "))
    card = int(input("Karta raqamini kiritng: "))
    my_card = int(input("Ozgizni kartangizni kiritng: "))

    my_balance = db.get_balance(my_card)
    if my_balance is None:
        print("Xato! Sizni kartangiz topilmadi.")
        return

    if my_balance < summ:
        print("Xato! Sizning hisobingizda yetarli mablag' mavjud emas.")
        return

    db.start_transaction()
    db.update_balance(card, summ)
    db.update_balance(my_card, -summ)
    db.commit()
    print(f"{name_to} ga {summ} sum pul o'tkazildi!")


def create_customer():
    name = input("Ismingizni kiriting: ")
    card_id = int(input("Kartangizni raqamini kiriting: "))
    balance = int(input("Hisobingizda bo'lgan summani kiriting: "))
    db.create_customer(name, card_id, balance)
    print("Yangi mijoz muvaffaqiyatli yaratildi!")


def show_all_customers():
    customers = db.get_all_customers()
    if customers:
        print("\nBarcha mijozlar va ularning balanslari:")
        for customer in customers:
            print(f"{customer[1]} (Karta raqami: {customer[2]}, Balans: {customer[3]} sum)")
    else:
        print("Hozircha hali mijozlar mavjud emas.")


def update_customer():
    card_id = int(input("Kartangizni raqamini kiriting: "))
    name = input("Yangi ismingizni kiriting: ")
    balance = int(input("Yangi balansingizni kiriting: "))
    db.update_customer(card_id, name, balance)
    print("Mijoz ma'lumotlari muvaffaqiyatli yangilandi!")


if __name__ == '__main__':
    print('''
    Assalomalkeum xurmatli mijoz 
    Ushbu loihada siz xisongizdagi pulni tekshirish 
    pulini otkazish kabi xizmatlardan foydalanishingiz mumkin
    buning uchun avvala royaxtadan oting
    ''')

    db = Database(database=database, user=user, host=host, password=password)

    while True:
        choose = int(input('''
        1. Balansni tekshirish
        2. Pul otkazish
        3. Yangi mijoz yaratish
        4. Barcha mijozlarni ko'rsatish
        5. Mijoz ma'lumotlarini yangilash

        Tanlang: '''))

        if choose == 1:
            check_balance()
        elif choose == 2:
            send_money()
        elif choose == 3:
            create_customer()
        elif choose == 4:
            show_all_customers()
        elif choose == 5:
            update_customer()
        else:
            print("Notog'ri qiymat kiriting;")
            continue
