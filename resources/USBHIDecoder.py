import csv

# HID scan code to ASCII (only basic letters/numbers for demo)
hid_map = {
    0x04: 'a', 0x05: 'b', 0x06: 'c', 0x07: 'd',
    0x08: 'e', 0x09: 'f', 0x0a: 'g', 0x0b: 'h',
    0x0c: 'i', 0x0d: 'j', 0x0e: 'k', 0x0f: 'l',
    0x10: 'm', 0x11: 'n', 0x12: 'o', 0x13: 'p',
    0x14: 'q', 0x15: 'r', 0x16: 's', 0x17: 't',
    0x18: 'u', 0x19: 'v', 0x1a: 'w', 0x1b: 'x',
    0x1c: 'y', 0x1d: 'z',
    0x1e: '1', 0x1f: '2', 0x20: '3', 0x21: '4',
    0x22: '5', 0x23: '6', 0x24: '7', 0x25: '8',
    0x26: '9', 0x27: '0',
    0x28: '\n',  # Enter
    0x2c: ' ',   # Space
    0x2d: '-', 0x2e: '=', 0x2f: '[', 0x30: ']',
    0x33: ';', 0x34: "'", 0x36: ',', 0x37: '.',
}

decoded_text = ""


# Update: Use first 2 bytes from Array, pad with two '00', use second byte as HID code

with open("E:\!packages\hiddenmsg\keystrokes.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        array_hex = row["Array"].strip()
        hid_data = row.get("HID Data", "").strip()
        shift = False
        if len(hid_data) >= 2 and hid_data[:2] == "02":
            shift = True
        if len(array_hex) >= 2:
            code = int(array_hex[:2], 16)
            if code in hid_map:
                char = hid_map[code]
                if shift and char.isalpha():
                    char = char.upper()
                decoded_text += char

print("Recovered keystrokes:\n", decoded_text)
