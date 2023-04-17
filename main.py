from io import StringIO

if __name__ == '__main__':
    locations = ['ห้องนั่งเล่น', 'ห้องนอน', 'ห้องน้ำ', 'ห้องครัว', 'สวนหลังบ้าน']
    topics = ['รูปภาพ', 'ตำแหน่งสิ่งของ', 'สิ่งลี้ลับ']
    sentences = '''
ไป l
ไป ที่ l
ดู l
ไป ดู l
ไป ดู ที่ l
ย้อน กลับ ไป ที่ l
สลับ กล้อง ไป ที่ l
l
ซ้าย
ขวา
ถัด ไป
ย้อน กลับ
รายงาน t
แจ้ง เรื่อง t
t
'''.strip().splitlines()

    results = StringIO()
    count = 1

    results.write(f'{count:04d} โกวาจี\n')

    for s in sentences:
        if 'l' in s:
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

    with open('transcripts.txt', 'w') as f:
        f.write(results.getvalue())
