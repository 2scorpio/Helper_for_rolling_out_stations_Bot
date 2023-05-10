# from keyboards import in_kb_help
#
# start_massage = f"Привет <b>{username}</b>, я могу:\n"
#                 '1 - Добавить новый сервер\n'
#                 '2 - Добавить камеры на действующий сервер\n'
#                 '3 - Изменить значение поля place_name (Только SQL)\n'
#                 '4 - Изменить значение поля camera (Только SQL)\n'
#                 '5 - Удалить данные в БД (Только SQL)\n'
#                 '6 - Обновить поля camera и place_name (С инвентори для перенастройки сервера)\n'
#                 '\n'
#                 'Для работы со мной нужно загрузить актуальны файл Metro.xlsx, '
#                 'в противном случае я буду использовать старые данные '
#                 'после выбора одного из действий вы получите 3 файла конфигурации.\n'
#                 '\n'
#                 '<b>Итак! Что вы хотите?</b>',
#                 reply_markup=in_kb_help


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def start_checker_zip(msg: Message, state: FSMContext):

    file_name = msg.document.file_name

    await msg.document.download(destination_file=os.path.join(CHECKER_TEMP_PATH, file_name))

    async with state.proxy() as data:
        try:
            if data['msg'] == 'Проверить все фото' and file_name.endswith('.zip'):
                workdir, paths_to_exel, json_response = await sync_to_async(Checker.checkAll)(filename=file_name)
                if isinstance(paths_to_exel, list) and json_response is None:
                    for exel in paths_to_exel:
                        await msg.answer_document(open(exel, 'rb'))
            # await sync_to_async(rmtree)(workdir)
            elif data['msg'] == 'Проверить 1 фото' and (file_name.lower().endswith('.jpg')
                or file_name.lower().endswith('.jpeg') or file_name.lower().endswith('.png')):
                message, errors, additional = await sync_to_async(Checker.checkAll)(filename=file_name)
                await msg.reply(f'{message}\n\n{errors}\n{additional}', parse_mode="html")
                await sync_to_async(os.remove)(os.path.join(CHECKER_TEMP_PATH, file_name))
            else:
                await msg.answer('Формат документа не поддерживается')
        except KeyError:
            await msg.answer('Вы не выбрали метод проверки')

        await state.finish()


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def start_checker_one_photo(msg: Message, state: FSMContext):
    photo_name = f'{msg.photo[-1].file_id}.jpg'
    async with state.proxy() as data:
        try:
            if data['msg'] == 'Проверить 1 фото':
                await msg.photo[-1].download(os.path.join(CHECKER_TEMP_PATH, photo_name))
                result, errors, json_response = await sync_to_async(Checker.checkAll)(filename=photo_name)
                await msg.reply(f'{result}\n\n{errors}\n{json_response}', parse_mode="html")
                await sync_to_async(os.remove)(os.path.join(CHECKER_TEMP_PATH, photo_name))
        except KeyError:
            await msg.answer('Вы не выбрали метод проверки')

        await state.finish()