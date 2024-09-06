import RPi.GPIO as GPIO
import time
import drivers  
SW1 = 27
SW2 = 17

current_member_index = 0  

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING, bouncetime=200)
GPIO.add_event_detect(SW2, GPIO.FALLING, bouncetime=200)


lcd = drivers.Lcd()

def display_lcd(name, std_id):
    lcd.lcd_clear()  
    lcd.lcd_display_string(f"{name}", 1)  
    lcd.lcd_display_string(f"{std_id}", 2)  


Group_mem = [
    {"name": "Jiradech Khumsiri", "std_id": "116630462032-9"},
    {"name": "Thanadol Jampatem", "std_id": "116630462033-7"},
    {"name": "Wanutchaphorn Thongkham", "std_id": "116630462034-5"}
]

try:
    while True:
        if GPIO.event_detected(SW1):  
            member = Group_mem[current_member_index]
            display_lcd(member["name"], member["std_id"])
            
            
            current_member_index = (current_member_index + 1) % len(Group_mem)  

        elif GPIO.event_detected(SW2):  
            lcd.lcd_clear()
            lcd.lcd_display_string(f"Bye...", 1)
            time.sleep(1)
            exit()  
 
        

except KeyboardInterrupt:
    pass

finally:
    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()
    lcd.lcd_clear()  
    print("\nBye...")
