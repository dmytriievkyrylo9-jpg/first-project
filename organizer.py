import os
import shutil

def organize_folder(target_dir):
    if not os.path.exists(target_dir):
        print(f"Помилка: Шлях {target_dir} не існує.")
        return

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.txt', '.docx', '.doc', '.xlsx', '.csv'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Scripts': ['.py', '.sh', '.js', '.cpp']
    }

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, exts in extensions.items():
            if file_ext in exts:
                category_dir = os.path.join(target_dir, category)
                os.makedirs(category_dir, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"Переміщено: {filename} -> {category}/")
                moved = True
                break

        if not moved:
            other_dir = os.path.join(target_dir, 'Other')
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"Переміщено в 'Other': {filename}")

if __name__ == "__main__":
    path_to_organize = input("Введіть шлях до папки для сортування: ").strip()
    organize_folder(path_to_organize)
