from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from sqlalchemy import select

from database.models import async_session, Task

router = Router()


@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer(text='Добро пожаловать в телеграм-бот «Книга памяти»!')


@router.message(Command('help'))
async def cmd_help(message: Message):
    help_txt = """Данный телеграм-бот предназначен для хранения, добавления и поиска информации о людях\n
Для запуска бота отправьте команду - '/start' """
    await message.answer(text=help_txt)


# @router.callback_query(F.data == 'add')
# async def search(callback: CallbackQuery, state: FSMContext):
#     await callback.answer('Для поиска в «Книге памяти» введите фамилию')
#     CallbackQuery.data
#     await callback.message.answer('Запись успешно добавлены')
#
#
# @router.message(Search.surname)
# async def cmd_search(message: Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     for_search = await state.get_data()
#     async with async_session() as session:
#         in_page = await session.execute(select(Page).where(Page.surname == for_search["surname"]))
#         res = in_page.all()
#         if not res:
#             await message.answer('Такой страницы пока не существует!', reply_markup=option_kb)
#         else:
#             for i in res:
#                 for j in i:
#                     await message.answer(f'{j}')
#             await message.answer(f'Найдено страниц: {len(res)}', reply_markup=option_kb)
#     await state.clear()
#
#
# @router.callback_query(F.data == 'new_page')
# async def new_page(callback: CallbackQuery, state: FSMContext):
#     await callback.answer('Вы приступаете к заполнению новой страницы в «Книге памяти»!')
#     await state.set_state(New_Page.surname)
#     await callback.message.answer('Введите фамилию:')
#
#
# @router.message(New_Page.surname)
# async def cmd_new_page_surname(message: Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     await state.set_state(New_Page.name)
#     await message.answer("Введите имя:")
#
#
# @router.message(New_Page.name)
# async def cmd_new_page_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(New_Page.patronymic)
#     await message.answer("Введите отчество:")
#
#
# @router.message(New_Page.patronymic)
# async def cmd_new_page_patronymic(message: Message, state: FSMContext):
#     await state.update_data(patronymic=message.text)
#     await state.set_state(New_Page.birthday)
#     await message.answer("Введите дату рождения (ДД.ММ.ГГГГ):")
#
#
# @router.message(New_Page.birthday)
# async def cmd_new_page_birthday(message: Message, state: FSMContext):
#     await state.update_data(birthday=message.text)
#     for_check = await state.get_data()
#     async with async_session() as session:
#         checking = await session.scalar(select(Page).where(Page.surname == for_check["surname"],
#                                                            Page.name == for_check["name"],
#                                                            Page.patronymic == for_check["patronymic"],
#                                                            Page.birthday == for_check["birthday"]))
#         if checking is not None:
#             await message.answer('Такая страница уже существует!', reply_markup=option_kb)
#             await state.clear()
#         else:
#             await state.set_state(New_Page.birthplace)
#             await message.answer("Введите место рождения:")
#
#
# @router.message(New_Page.birthplace)
# async def cmd_new_page_birthplace(message: Message, state: FSMContext):
#     await state.update_data(birthplace=message.text)
#     await state.set_state(New_Page.death_date)
#     await message.answer("Введите дату смерти (ДД.ММ.ГГГГ):")
#
#
# @router.message(New_Page.death_date)
# async def cmd_new_page_death_date(message: Message, state: FSMContext):
#     await state.update_data(death_date=message.text)
#     await state.set_state(New_Page.death_place)
#     await message.answer("Введите место смерти:")
#
#
# @router.message(New_Page.death_place)
# async def cmd_new_page_death_place(message: Message, state: FSMContext):
#     await state.update_data(death_place=message.text)
#     await state.set_state(New_Page.biography)
#     await message.answer("Введите биографию:")
#
#
# @router.message(New_Page.biography)
# async def cmd_new_page_biography(message: Message, state: FSMContext):
#     await state.update_data(biography=message.text)
#     await state.set_state(New_Page.obit)
#     await message.answer("Введите эпитафию:")
#
#
# @router.message(New_Page.obit)
# async def cmd_new_page_obit(message: Message, state: FSMContext):
#     await state.update_data(obit=message.text)
#     page = await state.get_data()
#     async with async_session() as session:
#         in_page = await session.scalar(select(Page).where(Page.surname == page["surname"],
#                                                           Page.name == page["name"],
#                                                           Page.patronymic == page["patronymic"],
#                                                           Page.birthday == page["birthday"]))
#         if in_page is None:
#             session.add(Page(surname=page["surname"],
#                              name=page["name"],
#                              patronymic=page["patronymic"],
#                              birthday=page["birthday"],
#                              birthplace=page["birthplace"],
#                              death_date=page["death_date"],
#                              death_place=page["death_place"],
#                              biography=page["biography"],
#                              obit=page["obit"]))
#             await session.commit()
#             await message.answer('Страница успешно добавлена!', reply_markup=option_kb)
#         else:
#             await message.answer('Кто-то опередил Вас при создании страницы! Воспользуйтесь поиском по «Книге памяти»',
#                                  reply_markup=option_kb)
#     await state.clear()