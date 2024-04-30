from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from sqlalchemy import select

from database.models import async_session, Task

router = Router()


class Add(StatesGroup):
    task = State()


@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer(text="Добро пожаловать в телеграм-бот «Список задач»!\n"
                              "Для получения справочной информации о работе бота отправьте команду - '/help'")


@router.message(Command('help'))
async def cmd_help(message: Message):
    help_txt = """Данный телеграм-бот предназначен для создания задач и вывода списка задач из бд\n
    Для запуска бота отправьте команду - '/start'\n
    Для создания задачи отправьте команду - '/add'\n
    Для вывода списка задач отправьте команду - '/tsk'"""
    await message.answer(text=help_txt)


@router.message(Command('add'))
async def add(message: Message, state: FSMContext):
    await state.set_state(Add.task)
    await message.answer('Введите задачу для добавления в базу данных')


@router.message(Add.task)
async def cmd_add(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    for_add = await state.get_data()
    async with async_session() as session:
        session.add(Task(tasks=for_add["task"]))
        await session.commit()
        await message.answer("Задача успешно добавлена!")
    await state.clear()


@router.message(Command('tsk'))
async def tsk(message: Message):
    async with async_session() as session:
        result = await session.execute(select(Task))
        tsk_list = [str(i[0]) for i in result.all()]
        await message.answer(f"{''.join(tsk_list)}")
