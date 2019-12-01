import os
import re
import json
from shutil import copy
from sys import exit as die
from PIL import Image
from resizeimage import resizeimage
from gallery_paths import data_files, data_folders


class Copier:
    src_path = ''  # backups folder path
    target_path = ''  # source/large
    latest_backup_path = ''  # backups/latest_folder
    latest_images = {}

    def __init__(self, src_path, target_path):
        self.src_path = src_path
        self.target_path = target_path
        self.latest_backup(self.src_path)
        self.checker()
        self.get_latest_images()

    @staticmethod
    def json_formatter(dict_text):
        result = re.sub(r'[ ]{4}', r'\t', dict_text)
        result = re.sub(r',\n\t\t\t', r', ', result)
        result = re.sub(r'\n\t\t\t', r'', result)
        result = re.sub(r'\n\t\t\]', r']', result)
        return result

    def latest_backup(self, backup_path):
        backups = []
        for i in os.listdir(backup_path):
            backups.append(i)

        # find last back up folder
        last = 0
        for i in backups:
            folder_name = int(i.replace('-', ''))
            if folder_name > last:
                last = folder_name
        last_backup_folder = str(last)[:8] + '-' + str(last)[8:]
        last_backup_folder = backup_path + '\\' + last_backup_folder
        self.latest_backup_path = last_backup_folder

    def checker(self):
        # check if folders names inside latest_backup_path conform the naming rule (\d\d\d\d .+)
        for folder in os.listdir(self.latest_backup_path):
            if not re.search(r'\d{4} .+', folder.strip()):
                print('[Warning] folder name does not conform the naming rule (\d\d\d\d .+): {}'.format(
                    last_backup_folder + '\\' + folder))
                die()

        # check if every folder contains only one thumbnail
        for folder in os.listdir(self.latest_backup_path):
            folder_path = self.latest_backup_path + '\\' + folder
            thumbnails = []
            for image in os.listdir(folder_path):
                if image.lower().startswith('thumbnail'):
                    thumbnails.append(image)
            if len(thumbnails) > 1:
                print('[Warning] {} folder contains more than one thumbnail, please find the right thumbnail'.format(
                    folder))
                die()
            elif len(thumbnails) == 0:
                print('[Warning] {} folder contain no thumbnail, please find the right thumbnail'.format(
                    folder))
                die()

    def get_latest_images(self):
        self.latest_images = []
        for folder in os.listdir(self.latest_backup_path):
            orig_images_path = self.latest_backup_path + '\\' + folder
            activity_folder = re.search(r'\d{1,4}', folder.strip()).group()
            self.latest_images.append({})
            self.latest_images[-1]["id"] = activity_folder
            self.latest_images[-1]["gallery_thumbnail"] = ''
            self.latest_images[-1]["photos"] = []
            for image in os.listdir(orig_images_path):
                if image != 'Thumbs.db':
                    if image.lower().startswith('thumbnail'):
                        self.latest_images[-1]["gallery_thumbnail"] = image
                    self.latest_images[-1]["photos"].append(image)

    def copy_to_local_large(self):
        for folder in os.listdir(self.latest_backup_path):
            new_folder_name = re.search(r'^\d{4}', folder).group()
            folder_path = self.latest_backup_path + '\\' + folder
            try:
                os.mkdir(self.target_path + '\\' + new_folder_name)
            except:
                pass
            for image in os.listdir(folder_path):
                if image != 'Thumbs.db':
                    src = folder_path + '\\' + image
                    dst = self.target_path + '\\' + new_folder_name + '\\' + image
                    copy(src, dst)

    def order_latest_images(self):
        id_sequence = []
        for block_index, block in enumerate(self.latest_images):
            self.latest_images[block_index]["photos"] = sorted(block["photos"], key=lambda x: x.lower())
            id_sequence.append(block["id"])

        # sort alphabetically
        id_sequence.sort()

        # sort by image size (vertical image at the end)
        for block_index, block in enumerate(self.latest_images):
            large_path = self.target_path + '\\' + block['id']
            normal_images = []
            vertical_images = []
            for image in os.listdir(large_path):
                for img in block['photos']:
                    if image == img:
                        if not img.lower().startswith('thumbnail'):
                            large_image = large_path + '\\' + img
                            im = Image.open(large_image)
                            width, height = im.size
                            if height > width:
                                vertical_images.append(img)
                            else:
                                normal_images.append(img)
                        break
            if len(vertical_images) != 0:
                self.latest_images[block_index]['photos'] = normal_images + [self.latest_images[block_index]['gallery_thumbnail']] + vertical_images
            else:
                self.latest_images[block_index]['photos'] = normal_images + [self.latest_images[block_index]['gallery_thumbnail']]

        new_order = []
        for e in id_sequence:
            for block in self.latest_images:
                if e == block["id"]:
                    new_order.append(block)
        new_order.append({})
        new_order[-1]["id"] = "notes"
        new_order[-1]["exist"] = []
        new_order[-1]["special_photos"] = []

        # check if there are special_photos,
        # if so, self.latest_images[-1]['special_photos'] is updated
        for block in self.latest_images:
            large_path = self.target_path + '\\' + block['id']
            for image in os.listdir(large_path):
                for img in block['photos']:
                    if image == img:
                        large_image = large_path + '\\' + img
                        im = Image.open(large_image)
                        width, height = im.size
                        if width > 1024:
                            new_order[-1]["special_photos"].append(
                                "{}/{} ({}W {}H)".format(block['id'], img, width, height))
                        break
        self.latest_images = new_order

    def update_current_gallery(self, cur_path, main_path):
        with open(main_path, 'r', encoding='utf-8') as file:
            file_content = json.loads(file.read())

        if len(file_content) == 0:
            new_file_content = json.dumps(self.latest_images, indent=4, ensure_ascii=False)
            new_file_content = self.json_formatter(new_file_content)
            with open(cur_path, 'w', encoding='utf-8') as file:
                file.write(new_file_content)
        else:
            # check if gallery_data_current.json id exists in gallery_data.json,
            # if so, self.latest_images[-1]['exist'] is updated
            for cur_block in self.latest_images:
                for main_block in file_content:
                    if cur_block["id"] == main_block["id"]:
                        self.latest_images[-1]['exist'].append(cur_block['id'])
            new_file_content = json.dumps(self.latest_images, indent=4, ensure_ascii=False)
            new_file_content = self.json_formatter(new_file_content)
            with open(cur_path, 'w', encoding='utf-8') as file:
                file.write(new_file_content)

    def resize_to_thumbnail(self, thumbnail_path):
        # 400px for thumbnail size image
        sizes = [400]

        for block in self.latest_images:
            if block['id'] != 'notes':
                new_folder_name = thumbnail_path + '\\' + block['id']
                large_path = self.target_path + '\\' + block['id']
                try:
                    os.mkdir(new_folder_name)
                except:
                    pass
                for image in os.listdir(large_path):
                    for img in block['photos']:
                        if image == img:
                            large_image = large_path + '\\' + img
                            im = Image.open(large_image)
                            width, height = im.size
                            if width <= 1024:
                                dst = new_folder_name + '\\' + img
                                im = resizeimage.resize_width(im, sizes[0])
                                im.save(dst, im.format)
                            break

    def copy_to_production(self, lp1, lp2, tp1, tp2):
        # copy from source/large to large
        for block in self.latest_images:
            if block['id'] != 'notes':
                new_folder_name = lp2 + '\\' + block['id']
                try:
                    os.mkdir(new_folder_name)
                except:
                    pass
                for image in block['photos']:
                    src = lp1 + '\\' + block['id'] + '\\' + image
                    dst = new_folder_name + '\\' + image
                    copy(src, dst)

        # copy from source/thumbnail to thumbnail
        for block in self.latest_images:
            if block['id'] != 'notes':
                new_folder_name = tp2 + '\\' + block['id']
                try:
                    os.mkdir(new_folder_name)
                except:
                    pass
                for image in block['photos']:
                    src = tp1 + '\\' + block['id'] + '\\' + image
                    dst = new_folder_name + '\\' + image
                    copy(src, dst)


# C:\Users\Raymond\Downloads

if __name__ == '__main__':
    local_backups_path = data_folders['program_backups']
    local_large_path = data_folders['program_large']

    copier = Copier(local_backups_path, local_large_path)
    copier.copy_to_local_large()  # copy image from latest backup to source/large
    copier.order_latest_images()  # sort latest_images
    copier.update_current_gallery(data_files['gallery_data_current_json'], data_files['gallery_data_json'])  # update gallery_data_current.json based on latest_images
    copier.resize_to_thumbnail(data_folders['program_thumbnail'])  # copy and resize images from source/large to source/thumbnail
    # copier.copy_to_production(data_folders['program_large'], data_folders['production_large'], data_folders['program_thumbnail'], data_folders['production_thumbnail'])  # resize all images before copy all latest images to production

