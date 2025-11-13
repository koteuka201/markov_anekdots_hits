import re

def process_anekdots(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Разделяем анекдоты по топику (словам типа "pro-sudey")
    # Ищем паттерн: топик, затем текст, затем цифра в конце
    pattern = r'[a-z\-]+\s+(.*?)\s+\d+(?=\s*[a-z\-]+\s+|$)'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    anekdots = []
    for match in matches:
        # Удаляем лишние переносы и пробелы, оставляем текст в одну строку
        cleaned = ' '.join(match.split())
        anekdots.append(cleaned)
    
    # Записываем в выходной файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for anekdot in anekdots:
            f.write(anekdot + '\n')
    
    print(f"Обработано {len(anekdots)} анекдотов")
    print(f"Результат сохранён в {output_file}")

# Использование
process_anekdots('anekdots_oneline.txt', 'anekdots_oneline2.txt')