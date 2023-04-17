from io import StringIO

if __name__ == '__main__':
    locations = ['ห้องนั่งเล่น', 'ห้องนอน', 'ห้องน้ำ', 'ห้องครัว', 'สวนหลังบ้าน']
    topics = ['รูปภาพ', 'ตำแหน่งสิ่งของ', 'สิ่งลี้ลับ', 'ไฟฟ้า', 'ผู้บุกรุก']
    sentences = '''
ไป l
ไป ที่ l
ดู l
ไป ดู l
ไป ดู ที่ l
กลับ ไป ที่ l
สลับ ไป l
สลับ ไป ที่ l
สลับ กล้อง ไป ที่ l
เช็ค l
ไป เช็ค l
ไป เช็ค ที่ l
เปลี่ยน ไป l
เปลี่ยน ไป ที่ l
เปลี่ยน
ต่อ ไป
ถัด ไป
ย้อน กลับ
รายงาน t
รายงาน t ที่ l
รายงาน l เรื่อง t
รายงาน เรื่อง t
รายงาน เรื่อง t ที่ l
รายงาน ที่ l เรื่อง t
'''.strip().splitlines()

    results = StringIO()
    count = 0

    results.write(f'{count:04d} โกวาจี\n')
    count += 1

    for s in sentences:
        if 'l' in s and 't' in s:
            for loc in locations:
                for topic in topics:
                    results.write(f'{count:04d} {s.replace("l", loc).replace("t", topic)}\n')
                    count += 1
        elif 'l' in s:
            for loc in locations:
                results.write(f'{count:04d} {s.replace("l", loc)}\n')
                count += 1
        elif 't' in s:
            for topic in topics:
                results.write(f'{count:04d} {s.replace("t", topic)}\n')
                count += 1
        else:
            results.write(f'{count:04d} {s}\n')
            count += 1

    print(results.getvalue())

    with open('transcripts.txt', 'w', encoding='utf8') as f:
        f.write(results.getvalue())
