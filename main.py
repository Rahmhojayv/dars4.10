# 1 masala
# class Talaba:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Kurs:
#     def __init__(self, kurs_name, kurs_teacher):
#         self.kurs_name = kurs_name
#         self.kurs_teacher = kurs_teacher
#         self.talabalar_soni = 0
#         self.talabalar = []
#     def add(self, new_student):
#         """Yangi talabani kursga qo'shish."""
#         self.talabalar.append(new_student)
#         self.talabalar_soni += 1
#     def delete(self, new_student):
#         """Talabani kursdan haydash."""
#         if new_student in self.talabalar:
#             self.talabalar.remove(new_student)
#             self.talabalar_soni -= 1
#     def info_kurs(self):
#         """Kurs haqida ma'lumot berish."""
#         print(f"Kurs nomi: {self.kurs_name}")
#         print(f"O'qituvchi: {self.kurs_teacher}")
#         print(f"Talabalar soni: {self.talabalar_soni}")
#         print("Talabalar:")
#         for talaba in self.talabalar:
#             print(f"- {talaba.name}, {talaba.age} yoshda")
# kurs1 = Kurs("Matematika", "Ali Rahmonov")
# kurs2 = Kurs("Informatika", "Dilorom Sattorova")
# talabalar = [Talaba(f"Talaba {i+1}", 20 + i) for i in range(10)]
# for talaba in talabalar:
#     kurs1.add(talaba)
# talabalar2 = [Talaba(f"Talaba {i+11}", 20 + i) for i in range(10)]
# for talaba in talabalar2:
#     kurs2.add(talaba)
# kurs1.delete(talabalar[0])
# kurs1.delete(talabalar[1])
# print("\n1-kurs haqida:")
# kurs1.info_kurs()
# print("\n2-kurs haqida:")
# kurs2.info_kurs()

# 2 masala
# class Telegram:
#     def __init__(self):
#         self.user_name = ""
#         self.send_chat_text = ""
#         self.accept_chat_text = ""
#         self.chat_status = ""
#         self.chat_time = ""
#
#     def input_user(self, user_name):
#         """Foydalanuvchi ismini kiritish."""
#         self.user_name = user_name
#     def send(self, receiver, message):
#         """Xabarni yuborish."""
#         receiver.accept_chat_text = message
#         receiver.chat_status = 'sending'
#     def read(self):
#         """Kelgan xabarni o'qish."""
#         if self.accept_chat_text:
#             print(f"{self.user_name} kelgan xabar: {self.accept_chat_text}")
#             self.chat_status = 'reading'
#     def delete(self):
#         """Kelgan xabarni o'chirish."""
#         if self.accept_chat_text:
#             self.accept_chat_text = ""
#             self.chat_status = 'deleting'
# user1 = Telegram()
# user2 = Telegram()
# user1.input_user("Ali")
# user2.input_user("Vali")
# user1.send(user2, "Salom, Vali!")
# user2.read()
# user2.delete()
# print(f"Xabar holati: {user2.chat_status}")

# 3 masala
# class Karta:
#     def __init__(self, card_name):
#         self.card_name = card_name
#     def input_card(self, card_name):
#         """Karta nomini kiritish."""
#         self.card_name = card_name
#     def display_card(self):
#         """Karta nomini chiqarish."""
#         print(f"Karta nomi: {self.card_name}")
#     def compare(self, other_card):
#         """Boshqa karta bilan solishtirish."""
#         card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
#                       '7': 7, '8': 8, '9': 9, '10': 10,
#                       'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#         current_card_value = card_order[self.card_name]
#         other_card_value = card_order[other_card.card_name]
#         if current_card_value > other_card_value:
#             return 1
#         elif current_card_value < other_card_value:
#             return -1
#         else:
#             return 0
# player1_card = Karta("7")
# player2_card = Karta("A")
# print("Player 1:")
# player1_card.display_card()
# print("Player 2:")
# player2_card.display_card()
# result = player1_card.compare(player2_card)
# if result == 1:
#     print("Player 1 g'olib!")
# elif result == -1:
#     print("Player 2 g'olib!")
# else:
#     print("Ikkala o'yinchi teng!")

# 4 masala
# class Alphabet:
#     def __init__(self, language, letters):
#         self.language = language          # Til
#         self.letters = letters            # Harflar ro'yhati
#     def display_letters(self):
#         """Alfavitning barcha harflarini chiqaradi."""
#         print(f"{self.language} alfavitidagi harflar: {', '.join(self.letters)}")
#     def count_letters(self):
#         """Alfavitdagi barcha harflarni sanaydi."""
#         return len(self.letters)
# class EngAlphabet(Alphabet):
#     def __init__(self):
#         super().__init__("Ingliz tili", [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)])
#         self.letters_count = len(self.letters)  # Harflar soni
#     def count_letters(self):
#         """Alfavitdagi barcha harflarni sanaydi."""
#         return self.letters_count
#     def is_valid_letter(self, letter):
#         """Kiritilgan harf Ingliz alfavitiga tegishli yoki yo'qligini aniqlaydi."""
#         return letter in self.letters
#     def example_sentence(self):
#         """Ingliz alfavitiga mos misol gap chiqaradi."""
#         return "A quick brown fox jumps over the lazy dog."
# latin_alphabet = Alphabet("Lotin tili", ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
# latin_alphabet.display_letters()
# print(f"Lotin alfavitidagi harflar soni: {latin_alphabet.count_letters()}")
# english_alphabet = EngAlphabet()
# english_alphabet.display_letters()
# print(f"Ingliz alfavitidagi harflar soni: {english_alphabet.count_letters()}")
# test_letter = 'g'
# if english_alphabet.is_valid_letter(test_letter):
#     print(f"{test_letter} harfi Ingliz alfavitiga tegishli.")
# else:
#     print(f"{test_letter} harfi Ingliz alfavitiga tegishli emas.")
# print(f"Misol gap: {english_alphabet.example_sentence()}")