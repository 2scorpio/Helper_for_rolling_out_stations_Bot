#!/usr/bin/python3

import os, os.path
from typing import Hashable
# import pandas as pd
import contextlib
import psycopg2
import hashlib
import json
import base64
import uuid
import pandas as pd
import numpy as np
import re
from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl
from aiogram import Bot, Dispatcher, types


def transliteration(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|j|k|l|m|n|o|p|r|s|t|u|f|h|c|ch|sh|shch||y||e|yu|ya'.split('|')
    trantab = {k: v for k, v in zip(cyrillic, latin)}
    newtext = ''
    for ch in text:
        casefunc = str.capitalize if ch.isupper() else str.lower
        newtext += casefunc(trantab.get(ch.lower(), ch))
    return newtext


while True:
    # if __name__ == '__main__':
    file = __file__
    locate = os.path.dirname(__file__)
    pwd = os.path.join(locate, 'data', 'Metro.xlsx')
    srv = os.path.join(locate, 'output', 'Server_FP.sql')
    stat = os.path.join(locate, 'output', 'STATION.text')
    ln = os.path.join(locate, 'output', 'Luna.text')
    dl = os.path.join(locate, 'output', 'Delete_Server_FP.sql')
    upnum = os.path.join(locate, 'output', 'UPDATE number.sql')
    upcam = os.path.join(locate, 'output', 'UPDATE camera.sql')
    # register = pwd
    instances = []
    cameras = []
    categories = []
    id_cameras = []
    descriptions = []
    invens = []
    name_servers = []
    lunas = []
    lines = []
    stations = []
    numbers = []
    i = 0
    se = 0
    st = 0
    t = 0
    pd.options.mode.chained_assignment = None
    df1 = pd.read_excel(pwd, sheet_name='Лист1')

    # for index, row in df1.iterrows():
    #     station = transliteration(str(row['Станция'].lower().rstrip()))
    #     line = transliteration(str(row['Линия'].lower()))

    day = int(input('Выберите нужный скрипт: '
                    '\n1.Добавление нового сервера'
                    '\n2.Добавление камеры на действующий сервер'
                    '\n3.Изменение значения поля place_name (Только SQL)'
                    '\n4.Изменение значения поля camera (Только SQL)'
                    '\n5.Удаление данных в БД (Только SQL)'
                    '\n6.Обновление полей camera и place_name (С инвентори для перенастройки сервера)'
                    '\n7.Прекратить выполнение скрипта \n'))

    for index, row in df1.iterrows():
        station = transliteration(str(row['Станция'].lower().rstrip().replace('. ', ' ').replace('  ', ' ').replace('.', ' ')))
        line = transliteration(str(row['Линия'].lower().rstrip().replace('. ', ' ').replace('  ', ' ').replace('.', ' ')))
        number = transliteration(str(row['NumberCam']))
        stations.append(station)
        lines.append(line)
        numbers.append(number)
        #print(str(next(reversed(numbers))))

    if day in [1, 2, 5, 6]:
        # Имя сервера
        for index, row in df1.iterrows():
            name_server = lines[se].replace('-', '_').replace(' ', '_')
            name_server += '_' + stations[se].replace('-', '').replace('—', '').replace(' ', '_') + '_v' + \
                           str(row['Номер сервера'])
            se = se + 1
            name_servers.append(name_server)
        # ID камеры (имя сервера + cam + номер сервера по порядку)
        for index, row in df1.iterrows():
            id_camera = lines[st].replace('-', '_').replace(' ', '_')
            id_camera += '_' + stations[st].replace('-', '').replace('—', '').replace(' ', '_') + '_v' + \
                str(row['Номер сервера']) + '_cam' + \
                str(row['NumberCam'])
            st = st + 1
            id_cameras.append(id_camera)
        # Название камеры турникета
        for index, row in df1.iterrows():
            if (row['Линия']) == 'МЦК':
                description = 'МЦК '
            elif (row['Линия']) == 'Река':
                description = 'Причал '
            elif (row['Линия']) == 'Аэро':
                description = 'Аэроэкспресс '
            elif (row['Линия']) == 'Моно':
                description = 'Монорельс '
            else:
                description = str(row['Линия']) + ' м.'

            description += str(row['Станция'].strip().replace("—", "-").replace('ё', 'е')) + ' турникет ' + \
                           str(row['№ турникета'])
            descriptions.append(description)

        for index, row in df1.iterrows():
            if day in [1, 2]:
                # 1 INSERT (Добавление инстанса в БД)
                instance = 'INSERT INTO face_pay_sync_var.vn_instance_ref' \
                           '(instance, vendor, required_for_account_status, scopes, extr_descr_role, extr_descr_version)' \
                           ' VALUES ('
                instance += str(row['Инстанс']).replace('.0', ' ') + ', \'vl\', false, array[\'vtb\'], 2, \'luna-4\');'
                instances.append(instance)

                # 2 INSERT (Добавление камеры в БД)
                camera = 'INSERT INTO face_pay_ref_var.camera_ref(camera, place_id, place_name, for_instances_only) ' \
                         'VALUES (\''
                camera += id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + '\', ' + \
                          str(row['Инстанс']).replace('.0', '') + \
                          str(row['NumberCam']).replace('.0', '') + ', \'' + descriptions[i] + '\', array[' + \
                          str(row['Инстанс']).replace('.0', '') + ']);'
                cameras.append(camera)

                # 3 INSERT (Добавление инстанса в список вендора)
                category = 'INSERT INTO face_pay_sync_var.vn_category_ref' \
                           '(vn_category_ref_id, instance, category, remote_category) ' \
                           'VALUES (nextval(\'face_pay_sync_var.vn_category_ref_seq\'), '
                category += str(row['Инстанс']).replace('.0', '') + ', 1, \'test-turnstile1\');'
                categories.append(category)

            elif day == 5:
                # 1 INSERT (Удаление инстанса из БД)
                instance = 'DELETE FROM face_pay_sync_var.vn_instance_ref where instance = '
                instance += str(row['Инстанс']).replace('.0', ' ') + ';'
                instances.append(instance)

                # 2 INSERT (Удаление камеры из БД по полю place_name)
                camera = 'DELETE FROM face_pay_ref_var.camera_ref where place_id = \''
                camera += str(row['Инстанс']).replace('.0', '') + str(row['NumberCam']).replace('.0', '') + '\';'
                cameras.append(camera)

                # 3 INSERT (Удаление инстанса из список вендора)
                category = 'DELETE FROM face_pay_sync_var.vn_category_ref where instance = '
                category += str(row['Инстанс']).replace('.0', '') + ';'
                categories.append(category)
                i = i + 1
            elif day == 6:
                # UPDATE (Изменение полей camera и place_id в БД по полю place_name)
                camera = 'UPDATE face_pay_ref_var.camera_ref set '
                camera += 'place_name = \'' + descriptions[i].replace('.0', '') + '\'' + ', '
                camera += 'camera = \'' + id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + '\''
                camera += ' where place_id = ' + str(row['Инстанс']).replace('.0', '') + \
                          str(row['NumberCam']).replace('.0', '') + ';'
                cameras.append(camera)

            # Создание настроечных параметров для конфигуратора luna
            if day in [1, 2, 6]:
                if (row['NumberCam']) == 1:
                    luna = '[\n    {\n        "filtering": {\n            "detection-pitch-threshold": 40,\n'
                else:
                    luna = '    {\n        "filtering": {\n            "detection-pitch-threshold": 40,\n'
                luna += '            "detection-roll-threshold": 30,\n             "detection-yaw-threshold": 40,\n' \
                        '             "min-score": 0.5187000036,\n             "mouth-occlusion-threshold": 0,\n' \
                        '             "yaw-collection-mode": 0,\n             "yaw-number": 1\n        },'
                luna += '\n        "health_check": {\n            "max_error_count": 10,\n            "period": 3600,\n' \
                        '            "retry_delay": 5\n        },\n'
                luna += '        "id": "' + id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + '",\n'
                luna += '        "input": {\n            "droi":[\n                70,\n' \
                        '                50,\n                650,\n                1100\n            ],'
                luna += '\n            "frame-processing-mode": "auto",\n            "numberOfFfmpegThreads": 1,\n'
                luna += '            "roi": [\n                100,\n' \
                        '                500,\n                825,\n                1200\n            ],\n'
                luna += '            "rotation": 0,\n            "transport": "tcp",\n            "url": "' + \
                        'rtsp://admin:A156324a@' + str(row['ip адрес\nтурникетной\nкамеры']) + ':554"\n        },'
                luna += '\n        "liveness": {\n            "liveness_mode": 1,\n' \
                        '            "liveness_threshold": 0.6000000238,\n            "livenesses_weights": [' \
                        '\n                0,\n                0.5,\n                0.5\n            ],'
                luna += '\n            "mask_backgrounds_count": 300,\n            "number_of_liveness_checks": 5,\n' \
                        '            "use_flying_faces_liveness_filtration": true,\n            "use_mask_liveness' \
                        '_filtration": true,\n            "use_shoulders_liveness_filtration": 0\n        },'
                luna += '\n        "name": "' + id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + '",\n' \
                        '        "output": {\n            "image_store_url": "",\n            "login": "loginExample",\n' \
                        '            "luna-account-id": "",\n            "password": "passwordExample",' \
                        '\n            "token": "deadbeef-0000-1111-2222-deadbeef0000",\n'
                if (row['NumberCam']) == 1:
                    luna += '            "url": "http://127.0.0.1:9000/receiver"\n        },\n'
                else:
                    luna += '            "url": "http://127.0.0.1:9000/receiver/fp' + \
                            str(row['NumberCam']).replace('.0', '').replace('1', '') + '"\n        },\n'
                luna += '        "primary_track_policy": {\n            "best_shot_min_size": 120,\n' \
                        '            "best_shot_proper_size": 500,\n            "use_primary_track_policy": true\n' \
                        '        },\n'
                luna += '        "sending": {\n            "number-of-bestshots-to-send": 1,\n' \
                        '            "silent-period": 0,\n            "time-period-of-searching": 1,\n' \
                        '            "type": "sec"\n        }\n    }'
                if (row['NumberCam']) == 1 and int(next(reversed(numbers))) > 1:
                    luna += ','
                elif str(row['NumberCam']) > str(next(reversed(numbers))):
                    luna += ',\n'
                else:
                    luna += '\n]'
                lunas.append(luna)

            # Файл для инвентора:
            if day in [1, 6]:
                if (row['NumberCam']) == 1:  # Если это первая камера на станции, которую подключают к ФП
                    inven = '[' + name_servers[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + ']\n' + \
                            str(row['ip miniFP']) + '\n[' + \
                            name_servers[i].replace('_s_v', '_sv').replace('_yu_v',
                                                                           '_uv') + ':vars]\n' + 'vendorInstance=' + \
                            str(row['Инстанс']).replace('.0', ' ')
                    inven += '\ngateLockHost' + str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                             str(row['ip адрес КЗП\nТурникета']) + '\nvendorOverrideCamera' + \
                             str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                             id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv')
                    inven += '\nrtspur' + str(row['NumberCam']).replace('.0', '').replace('1',
                                                                                          '') + '=rtsp://admin:A156324a@' + \
                             str(row['ip адрес\nтурникетной\nкамеры']) + ':554\n' + 'ipcam' + \
                             str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                             str(row['ip адрес\nтурникетной\nкамеры'])
                    inven += '\nmetroname=' + str(row['Вестибюль']) + '\nhostnm_id="{{ group_names[0] }}"\nnamecam' + \
                             str(row['NumberCam']).replace('.0', '').replace('1', '') + '="{{ vendorOverrideCamera' + \
                             str(row['NumberCam']).replace('.0', '').replace('1', '') + ' }}"'
                    invens.append(inven)
                    i = i + 1
                else:  # Если это 2,3 и т.д. камера на станции, которую подключают к ФП
                    inven = 'gateLockHost' + str(row['NumberCam']).replace('.0', '') + '=' + \
                            str(row['ip адрес КЗП\nТурникета']) + '\nvendorOverrideCamera' + \
                            str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                            id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv')
                    inven += '\nrtspur' + str(row['NumberCam']).replace('.0', '') + '=rtsp://admin:A156324a@' + \
                             str(row['ip адрес\nтурникетной\nкамеры']) + ':554\n' + 'ipcam' + \
                             str(row['NumberCam']).replace('.0', '') + '='
                    inven += str(row['ip адрес\nтурникетной\nкамеры']) + '\nnamecam' + \
                             str(row['NumberCam']).replace('.0', '') + '="{{ vendorOverrideCamera' + \
                             str(row['NumberCam']).replace('.0', '') + ' }}"'
                    invens.append(inven)
                    i = i + 1
            elif day == 2:
                inven = '[' + name_servers[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + ']\n' + \
                        str(row['ip miniFP']) + '\n[' + name_servers[i].replace('_s_v', '_sv').replace('_yu_v',
                                                                                                       '_uv') + ':vars]\n' + 'vendorInstance=' + \
                        str(row['Инстанс']).replace('.0', ' ')
                inven += '\ngateLockHost' + str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                         str(row['ip адрес КЗП\nТурникета']) + '\nvendorOverrideCamera' + \
                         str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + id_cameras[i].replace('_s_v',
                                                                                                                '_sv').replace(
                    '_yu_v', '_uv')
                inven += '\nrtspur' + str(row['NumberCam']).replace('.0', '').replace('1',
                                                                                      '') + '=rtsp://admin:A156324a@' + \
                         str(row['ip адрес\nтурникетной\nкамеры']) + ':554\n' + 'ipcam' + \
                         str(row['NumberCam']).replace('.0', '').replace('1', '') + '=' + \
                         str(row['ip адрес\nтурникетной\nкамеры'])
                inven += '\nmetroname=' + str(row['Вестибюль']) + '\nhostnm_id="{{ group_names[0] }}"\nnamecam' + \
                         str(row['NumberCam']).replace('.0', '').replace('1', '') + '="{{ vendorOverrideCamera' + \
                         str(row['NumberCam']).replace('.0', '').replace('1', '') + ' }}"'
                invens.append(inven)
                i = i + 1

        categories = list(set(categories))  # удаление дубликатов в 3 INSERT
        instances = list(set(instances))  # удаление дубликатов в 1 INSERT

        if day in [1, 3, 6]:
            # Cоздание файла sql, который отправляется администатору баз данных для добавления новых станция в БД
            with open(srv, "w", encoding='UTF-8')as fp:
                for instance in instances:
                    fp.write(instance + "\n")
                for camera in cameras:
                    fp.write(camera + "\n")
                for category in categories:
                    fp.write(category + "\n")

            # Создание файла STATION.text, который отправляется системному инженеру для внесения новых стнация в инвентор
            with open(stat, "w")as fp:
                for inven in invens:
                    fp.write(inven + "\n\n")

            with open(ln, "w")as fp:
                for luna in lunas:
                    fp.write(luna + "\n")

        elif day == 5:
            # Cоздание файла sql, который отправляется администатору баз данных для удаления станции в БД
            with open(dl, "w", encoding='UTF-8')as fp:
                for instance in instances:
                    fp.write(instance + "\n")
                for camera in cameras:
                    fp.write(camera + "\n")
                for category in categories:
                    fp.write(category + "\n")
            print('Обратие внимание, что удаление происходит во всех трёх таблицах, '
                  'удалите ненужные значения в скрипте при необходимости')
            input('Нажмите Enter для подтверждения, что вы осведомлены о рисках')
        elif day == 2:
            with open(srv, "w", encoding='UTF-8')as fp:
                for camera in cameras:
                    fp.write(camera + "\n")

            with open(stat, "w")as fp:
                for inven in invens:
                    fp.write(inven + "\n\n")

            with open(ln, "w")as fp:
                for luna in lunas:
                    fp.write(luna + "\n")
        break

    elif day == 3:
        # Название камеры турникета
        for index, row in df1.iterrows():
            if (row['Линия']) == 'МЦК':
                description = 'МЦК '
            elif (row['Линия']) == 'Река':
                description = 'Причал '
            elif (row['Линия']) == 'Аэро':
                description = 'Аэроэкспресс '
            elif (row['Линия']) == 'Моно':
                description = 'Монорельс '
            else:
                description = str(row['Линия']) + ' м.'
            description += str(row['Станция'].strip().replace("—", "-").replace('ё', 'е')) + ' турникет '
            description += str(row['№ турникета'])
            descriptions.append(description)

        # UPDATE face_pay_ref_var.camera_ref set place_name = 'place_name' where place_id = 111111;
        for index, row in df1.iterrows():
            # UPDATE (Изменение нумерации в БД по полю place_name)
            camera = 'UPDATE face_pay_ref_var.camera_ref set '
            camera += 'place_name = \'' + descriptions[i].replace('.0', '') + '\''
            camera += ' where place_id = ' + str(row['Инстанс']).replace('.0', '') + \
                      str(row['NumberCam']).replace('.0', '') + ';'
            cameras.append(camera)

        # Cоздание файла UPDATE number.sql, который отправляется администатору баз данных для обновления данных в БД
        with open(upnum, "w", encoding='UTF-8')as fp:
            for camera in cameras:
                fp.write(camera + "\n")
        break

    elif day == 4:
        # ID камеры (имя сервера + cam + номер сервера по порядку)
        for index, row in df1.iterrows():
            if stations[st].count(' ') > 1:
                id_camera = lines[st].replace('-', '_').replace(' ', '_')
                id_camera += '_' + stations[st].replace(" ", "").replace("_", "-").replace("—", "_") + '_v' + \
                             str(row['Номер сервера']) + '_cam' + \
                             str(row['NumberCam'])
            else:
                id_camera = lines[st].lower().replace('-', '_').replace(' ', '_')
                id_camera += '_' + stations[st].lower().replace(" ", "_").replace("-", "_").replace("—", "_") + '_v' + \
                             str(row['Номер сервера']) + '_cam' + \
                             str(row['NumberCam'])
            id_cameras.append(id_camera)
            st = st + 1

        # UPDATE face_pay_ref_var.camera_ref set camera = 'camera' where place_id = 111111;
        for index, row in df1.iterrows():
            # UPDATE (Изменение в БД поля camera по полю place_id)
            camera = 'UPDATE face_pay_ref_var.camera_ref set '
            camera += 'camera = \'' + id_cameras[i].replace('_s_v', '_sv').replace('_yu_v', '_uv') + '\''
            camera += ' where place_id = ' + str(row['Инстанс']).replace('.0', '') + str(row['NumberCam']).replace(
                '.0', '') + ';'
            cameras.append(camera)
            i = i + 1

        # Cоздание файла UPDATE camera.sql, который отправляется администатору баз данных для обновления данных в БД
        with open(upcam, "w", encoding='UTF-8')as fp:
            for camera in cameras:
                fp.write(camera + "\n")
        break

    elif day == 7:
        break

    else:
        print('Введите число от 1 до 7')
SystemExit(1)

# V3.3 Исправил формирование поля name в файле Luna
# V3.4 Исправлены ошибки при формировании скрипта Luna
# v3.5 Исправлены ошибки формирования имени сервера и камер

# v3.6 Исправленные проблемы:
# а) Исправлена проблема, из-за которой запуск на MacOS был проблемным
# б) Исправлены ошибки в скриптах 3, 4, 5 и 6
# в) Улучщена читаемость кода

# v3.7 Теперь в файле STATION после gateLockHost ставится "=" для лучшего чтения.
# Настроено правильное построение наименования турникета для монорельса

# V4 Теперь для второго сценария в sql файл не добавляется инстанс, т.к. он должен уже существовать
# В файле Luna в конце не должна ставиться запятая

# V5 1) Убраны ошибки при формировании имени камеры и сервера:
# 1.1) Если есть точка, и после пробел, точку убираем
# 1.2) Если есть только точка, то заменяем на пробел
# 1.3) Если несколько отступов, то они будут заменены на один
# 1.4) Испрввлен баг с написанием всех слов слитно
# 2) Теперь в наименовании турникета буквы Ё заменяются на Е =)
