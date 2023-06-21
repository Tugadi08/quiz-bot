import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from inline import *

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum\nTest botiga xush kelibsiz!\nPastdagi variantlardan birortasini tanlab testni ishlashingiz mumkun😉.", reply_markup=gg_menu)



@dp.callback_query_handler(text="1")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Merhamat👍", reply_markup=fan_menu)






# 1. MATEMATIKA



@dp.callback_query_handler(text="2")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.12 + 12 x 10",
        options=["132", "240", "262"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.18 x 9",
        options=["156", "148", "162"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.2 x 2",
        options=["4", "5", "3"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.14 x 17",
        options=["238", "248", "228"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.1 + 1 + 1 - 3 + 2 - 9 * 2 + 3",
        options=["-13", "13", "0"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.7 + 9 + 3 + 6 - 9 - 0 - 6 - 9 + 6 * 1 - 8",
        options=["0", "1", "-1"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.12 + 12 x 10",
        options=["132", "240", "262"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.17 - 69 + 85 * 2 - 79 - 96 + 57",
        options=["51", "15", "0"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.18 - 96 + 47 + 56 + 39 - 9",
        options=["55", "78", "30"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="10.995 - 556 - 456 + 2520",
        options=["3295", "2503", "2864"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    , reply_markup=fan_menu)







# 2. FIZRA




@dp.callback_query_handler(text="3")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.Jismoniy tarbiya va sport to‘g‘risidagi qonun qachon qabul qilingan?",
        options=["1991", "1993", "1992"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.Yangi tahrirdagi oxirgi jismoniy tarbiya va sport to‘g‘risidagi qonun qachon qabul qilindi?",
        options=["2015", "2014", "2016"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.Basketbol maydonining o‘lchami qancha?",
        options=["28m x 15m", "30m x 15m", "15m x 15m"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.Osiyo o‘yinlari federatsiyasi qachon tashkil etilgan",
        options=["1947", "1946", "1949"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.«Atlet» so‘zining maonosi",
        options=["O'rtacha(Norm)", "Qiltiriq", "Kachok"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.Afrika o‘yinlari federatsiyasi qachon tashkil topgan?",
        options=["1975", "1965", "1985"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.Badminton o‘yinida erkaklar necha hisobgacha o‘ynaladi",
        options=["13", "15", "11"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.«Suv polosi» sport turida nechta o‘yinchi ishtirok etadi?",
        options=["7", "11", "9"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.Sakrash chuqurchasining uzunasi qancha?",
        options=["6", "10", "8"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="10.Ayollar to‘siqlarning balandligi qancha",
        options=["74", "84", "64"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    , reply_markup=fan_menu)








# 3. LITERATURA




@dp.callback_query_handler(text="4")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.Badiiy adabiyotning asosiy ish qurolini aniqlang",
        options=["Tuy'gu", "Fikr", "So'z"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.Qurruyo- qur hayt –a to‘ramning oti” tarzidagi nola kimga tegishli?",
        options=["Qaldirg‘ochga", "Oybarchinga", "Qultoyga"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.Adabiy turlarning bo‘linishi qaysi qatorda to‘g‘ri berilgan?",
        options=["Lirik, epik, komedik", "Dramatik, epik, satirik", "She’riy, nasriy, sahnaga"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.Qadimgi rivoyatlarga ko‘ra birinchi she’r muallifi qaysi qatorda to‘g‘ri berilgan?",
        options=["Odam ato", "Xalq", "Aristotel"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.O‘zligidan voz kechmaydigan millat qanday xususiyatga ega bo‘lishi shart?",
        options=["Milliy ruhiyatiga", "Milliyligiga", "Urf- odatiga"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.Tegra so‘zining lug‘aviy manosini aniqlang",
        options=["Oyoq", "Cho‘l", "Atrof"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.Adabiyot ilmida saj qanday ataladi?",
        options=["She’riy san’at", "Nasrdagi ichki qofiya", "Nazimdagi ichki qofiya"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.Xamsachilikni boshlab bergan ulug‘ xamsanavisni aniqlang.",
        options=["Sheroziy", "Jomiy", "Ganjaviy"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.Nizomiyning “Maxzan ul-asror” hamdnomasi kimga bag‘ishlangan?",
        options=["Firdavsiyga", "Jomiyga", "Faxriddin Bahromshohg"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="10.Buyuk xansanavis Xusrav Dehlaviyning asl vatani qayer edi?",
        options=["Dehli", "Samarqand", "Shaxrisabiz"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    , reply_markup=fan_menu)







# 4. XIMIYA




@dp.callback_query_handler(text="5")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.Davrlarda elementlar tartib raqamining ortib borishi bilan elementlaming elektrmanfiyligi qanday o'zgaradi?",
        options=["Ortadi", "Kamayadi", "Faqat katta davrlarda ortadi"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.Qaysi element atomi bitta elektronni oson beradi?",
        options=["Ba", "Rb", "K"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.Qaysi elementning metallik xossalari kuchliroq?",
        options=["Al", "Ag,", "Mg"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.Qaysi elementning metallmaslik xossalari kuchliroq?",
        options=["Si", "F", "N"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.Qaysi elementning elektnnanfiyligi katta?",
        options=["F", "O", "C"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.Qaysi elementning elektnnanfiyligi kichik?",
        options=["Rb", "Li", "Cs"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.Atom tuzilishi quyidagicha bo'lgan qaysi elementning metallik xossalari kuchli ifodalangan?",
        options=["...2s'", " ...3s'", " ...4s'"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.Quyidagilardan qaysi bin tabiatda eng barqaror vodorodii birikma ekanligini ko'rsating.",
        options=["CaH", "H O", "H Te"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.Qaysi qatorda faqat qutbsiz kovalent bog'lanishli moddalar formulasi keltirilgan?",
        options=["N, CuO, Cl", "H, N, O", "NaCI, H, SO"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="10.Vodorod peroksidda kislorodning oksidlanish darajasi nechaga teng?",
        options=["+2", "+1", "-1"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    , reply_markup=fan_menu)







# 5. BOLOGIYA



@dp.callback_query_handler(text="4")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.Biologiyani o`rganish usullari qaysilar?",
        options=["Eksperimental,ekologik", "Kuzatish,laboratoriya,nazariy", "Kuzatish,tarixiy,eksperimenta"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.Biologoyani kuzatish usuli orqali nimalar o`rganiladi?",
        options=["Biologik hodisalarni tasvirlash", "Tirik organizmlarni miqdor ko`rsatkichlari", "Tirik organizmlarni sifat ko`rsatkichlari"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.Taqqoslash usuli orqali nimalar o`rganiladi?",
        options=["Predmetlarni o`zaro taqqoslash", "Bir xil predmet hodisalarni bir-biridan farqi", "Hodisalarni o`zaro taqqoslash"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.Tarixiy usul orqali nimalar o`rganiladi?",
        options=["Irsiyat va o`zgaruvchanlik", "Xar-xil biologik hodisalar", "Tirik tabiatning rivojlanishi"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.Tirik organizmlarga xos belgilar qaysilar?",
        options=["Qo`zg`aluvchanlik,o`z-o`zini boshqarish,ko`payisha", "Harakatlanish,moddalar almashinuvi", "Yemirilish,harakatlanish"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.Moddalar almashinuvi deganda nimani tushunasiz",
        options=["Organizmlarning o`sish jarayoni", "Tashqi muhitdan oziq moddalar olishi", "Organizm bilan tashqi muhit o`rtasidagi munosabat"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.Biogeotsinoz nima?",
        options=["Tiriklikning yuqori darajasit", "Har-xil organizmlarning yashash muhiti bilan bog`lanishi", "Avtotrof va geterotroflar"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.Bakteriyalar shakliga ko`ra qanday ko`rinishlarda bo`ladi?",
        options=["Buralgan,zanjirsimon,x-simon", "Spiralsimon,noaniq chegarali", "Sharsimon,tayoqchasimon,buralgan"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.O`lat bakteriyalari qanday tarqaladi?",
        options=["Kemiruvchilarda yashovchi burgalar orqali", "Bitlar orqali", "Suv orqali"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="10.Qaysi kasalliklarda emlash yo`li bilan profilaktika olib boriladi?",
        options=["Ko`k yo`tal,qaqshal,defteriya", "Xolera,o`lat,ichburug`", "Meningit,ORVI,tif"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    , reply_markup=fan_menu)








# 6. ANGLIYSKI




@dp.callback_query_handler(text="5")
async def send_welcome(call: types.CallbackQuery):

    # 1 - savol
    await call.message.answer_poll(
        question="1.Brad and Marilyn are _____ honeymoon",
        options=["on", "at", "of"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 2 - savol
    await call.message.answer_poll(
        question="2.Wait _____ me",
        options=["on", "to", "for"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 3 - savol
    await call.message.answer_poll(
        question="3.Has she won the Wimbledon Tennis Tournament _____ ?",
        options=["already", "yet", "just"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 4 - savol
    await call.message.answer_poll(
        question="4.Have they _____ been to Australia?",
        options=["ever", "yet", "just"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 5 - savol
    await call.message.answer_poll(
        question="5.Qaysi elementning elektnnanfiyligi katta?",
        options=["Did", "Have", "Does"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(5)

    # 6 - savol
    await call.message.answer_poll(
        question="6.‘Hamlet’ is a play _____ Shakespeare",
        options=["on", "of", "by"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 7 - savol
    await call.message.answer_poll(
        question="7.Monica _____ many tournaments?",
        options=["have/won", "has/won", "has/win"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 8 - savol
    await call.message.answer_poll(
        question="8.She works _____ a big company.",
        options=["with", "to", "for"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 9 - savol
    await call.message.answer_poll(
        question="9.She has _____ to Portugal",
        options=["be", "been", "being"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(5)


    # 10 - savol
    await call.message.answer_poll(
        question="_____ they go to Australia last month?",
        options=["Do", "Did", "Have"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    , reply_markup=fan_menu)




@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)