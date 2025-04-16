
##
# رمز سزار را اجرا کنیدکه تمام حروف یک پیام را با مقدار حروف ارائه شده جا به جا کند
#از یک کاربر برای رمز گشایی از یک پیام از یک مقدار تغییر منفی استفاده منید
#
# پیغام را بخوانید و مقدار را ازکاربر دریافت کنید
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
# هرکارکتر را برای ساخت پیام رمز گذاری شده(رمز گشایی) پردازش کنید 
new_message = ""
for ch in message:
    if ch>= "a" and ch<= "z":
        # یک حرف کوچک را باتعیین آن پردازش کنید
        #مساحبه کنید  موقعیت در حروف الفبارا(25-0)  
        # موقعیت جدید و اقزودن آن به پیام جدید
        pos = ord(ch) - ord("a")
        pos = (pos+shift) % 25
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
        #مساحبه کنید  موقعیت در حروف الفبارا(25-0)  
        # موقعیت جدید و اقزودن آن به پیام جدید
        pos = ord(ch) - ord("A")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    else:
  new message = new message + ch
        # اگر کارکتر یک حرف نیست آن را در پیام جدید کپی کنید
	
# نمایش پیام تغییر یافته
print("The shifted message is", new_message)
