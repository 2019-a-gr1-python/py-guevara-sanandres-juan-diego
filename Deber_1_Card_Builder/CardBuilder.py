import curses, os
import os.path 
from curses.textpad import Textbox, rectangle

screen = curses.initscr() 
curses.noecho() 
curses.cbreak()  
curses.start_color()
screen.keypad(1) 

def title_deployment(subtitle):
    screen.clear() 
    screen.border(0)
    screen.addstr(2,2, "Yugi-Oh Card Builder", curses.A_STANDOUT) 
    screen.addstr(4,2, subtitle, curses.A_BOLD)

def topmenu():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_RED, curses.COLOR_YELLOW)
  pos=1 
  x = None 
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    title_deployment("Selecciona una opcion...")
    display_titles_menu(n,"1 - CARTAS","2 - TIPOS DE CARTAS","3 - Exit",5,6,7)
    s = Higlight_Text_Menu()
    s.indirect(pos,h,"1 - CARTAS","2 - TIPOS DE CARTAS","3 - Exit",5,6,7)
    screen.refresh()
    x = screen.getch()
    pos = move_button(x,pos,1,3)
  return ord(str(pos))

def move_button(x,pos,min,max):
    if x == 258:
      if pos < max:
        pos += 1
        return pos
      else: 
        pos = min
        return pos
    elif x == 259:
      if pos > min:
        pos += -1
        return pos
      else: 
        pos = max
        return pos
    elif x != ord('\n'):
      curses.flash()
      return min
    elif x == ord('\n'):
        return pos

def display_titles_menu(n,lb_1,lb_2,lb_3,pos1,pos2,pos3):
    screen.addstr(pos1,4,lb_1, n)
    screen.addstr(pos2,4,lb_2, n)
    screen.addstr(pos3,4,lb_3, n)

class Higlight_Text_Menu(object):
    def indirect(self,i,h,lb_1,lb_2,lb_3,pos1,pos2,pos3):
        method_name='number_'+str(i)
        method = getattr(self,method_name,lambda : 'Invalid')
        return method(h,lb_1,lb_2,lb_3,pos1,pos2,pos3)
    def number_1(self,h,lb_1,lb_2,lb_3,pos1,pos2,pos3):
        screen.addstr(pos1,4,lb_1, h)
    def number_2(self,h,lb_1,lb_2,lb_3,pos1,pos2,pos3):
        screen.addstr(pos2,4,lb_2, h)
    def number_3(self,h,lb_1,lb_2,lb_3,pos1,pos2,pos3):
        screen.addstr(pos3,4,lb_3, h)  

def submenu1(subtitle):
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_RED, curses.COLOR_YELLOW)
  pos=1
  x = None
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    title_deployment("Selecciona una accion para "+subtitle)
    display_titles_menu(n,"1 - Crear","2 - Buscar","3 - Retornar al menu principal",5,6,7)
    s = Higlight_Text_Menu()
    s.indirect(pos,h,"1 - Crear","2 - Buscar","3 - Retornar al menu principal",5,6,7)
    screen.refresh()
    x = screen.getch()
    pos = move_button(x,pos,1,3)
  return ord(str(pos))

def sub_menu(sub1get,subtitle):
    sub2get = None
    while sub2get !=ord('3'): 
        sub2get = submenu1(subtitle) 
        if sub2get != ord('3'): 
            s = Select_Action(sub1get,subtitle)
            s.indirect(sub2get)
    sub2get = None

class Select_Action(object):
    id = None
    subtitle = None
    def __init__(self,id,subtitle):
        self.id = id
        self.subtitle = subtitle
    def indirect(self,i):
        method_name='number_'+str(i-48)
        method = getattr(self,method_name,lambda : 'Invalid')
        return method()
    def number_1(self):
        create(self.id,self.subtitle,"crear")
    def number_2(self):
        find(self.id,self.subtitle,"buscar")

def create(id,subtitle,name_function):
    title_deployment("Escriba el nombre de "+subtitle+" que desea "+name_function+", para guardar el texto presione Enter")
    name = input()
    path =  "./CardTypes/"
    if(id==2):
        if(validate_type_card_name(name)):
            complete_name_file = os.path.join(path,name+".txt")
            with open(complete_name_file, 'a'):
                os.utime(complete_name_file, None)
        else:
            error_message(id,1)
    if(id==1):
        title_deployment("Escriba a que tipo de carta pertenece su nueva carta")
        card_type_name = input()+".txt"
        if(os.path.exists(path+card_type_name)):
            title_deployment("Ataque de la carta, Solo se acepta numeros")
            card_attack = input()
            title_deployment("Defensa de la carta, Solo se acepta numeros")
            card_defense = input()
            title_deployment("Nivel de estrellas de la carta, 1-10")
            stars_level = input()
            card_info = name+","+card_attack+","+card_defense+","+stars_level
            complete_name_file = os.path.join(path,card_type_name)
            f = open(complete_name_file,"a+")
            if(os.path.getsize(complete_name_file) > 0):
                f.write("\n")
                f.write(card_info)
            else:
                f.write(card_info)
            f.close()
        else:
            error_message(id,2)


def find(id,subtitle,name_function):
    title_deployment("Escriba el nombre de "+subtitle+" que desea "+name_function+", para guardar el texto presione Enter")
    name = input()
    path =  "./CardTypes/"
    if(id==1):
        title_deployment("Escriba a que tipo de carta pertenece su carta")
        card_type_name = input()+".txt"
        if(os.path.exists(path+card_type_name)):
            complete_name_file = os.path.join(path,card_type_name)
            f = open(complete_name_file,"r")
            f_lines = f.readlines()
            for l in f_lines:
                line_data = l.split(',')
                if(name.lower()==line_data[0].lower()):
                    getin = None
                    f.close()
                    while getin !=ord('7'): 
                        getin = edit_eliminate_selection1(line_data)
                        if getin != ord('7'): 
                            s = Select_Action2(id,line_data,complete_name_file)
                            s.indirect(getin)
                            getin = ord(str(s.getin))
    if(id==2):
        card_type_name = name+".txt"
        if(os.path.exists(path+card_type_name)):
            complete_name_file = os.path.join(path,card_type_name)
            f = open(complete_name_file,"r")
            f_lines = f.readlines()
            f.close()
            getin = None
            while getin != 7: 
                getin = edit_eliminate_selection2(f_lines,flag=True)
                if getin != 7: 
                    s = Select_Action2(id,"",complete_name_file)
                    s.indirect(getin+48)
                    getin = s.getin
            
        
                    
class Select_Action2(object):
    getin = None
    id = None
    line_data = None
    complete_name_file = None
    def __init__(self,id,line_data,complete_name_file):
        self.id = id
        self.line_data = line_data
        self.complete_name_file = complete_name_file
        self.getin = 0
    def indirect(self,i):
        method_name='number_'+str(i-48)
        method = getattr(self,method_name,lambda : 'Invalid')
        return method()
    def number_5(self):
        edit(self.id,self.line_data,self.complete_name_file)
    def number_6(self):
        eliminate(self.id,self.line_data,self.complete_name_file)   
        self.getin = 7
        
def edit(id,line_data,complete_name_file):
    path =  "./CardTypes/"
    if(id==1):
        getin = None
        while getin !=ord('9'): 
            getin = edit_selection(line_data)
            if getin != ord('9'):
                title_deployment("Cambiar "+line_data[getin-53]+" por")
                new_data = input()
                with open(complete_name_file,'r') as f:
                    f_lines = f.readlines()
                with open(complete_name_file,'w+') as f:
                    for l in f_lines:
                        line_data2 = l.split(',')
                        if(line_data[0]==line_data2[0]):
                            line_data2[getin-53] = new_data
                            f.write(line_data2[0]+","+line_data2[1]+","+line_data2[2]+","+line_data2[3])
                        else:
                            f.write(l)
                    f.close()
    if(id==2):
        title_deployment("Escriba el nombre del nuevo Tipo de Carta, para guardar el texto presione Enter")
        name = input()+".txt"
        new_name_file = os.path.join(path,name)
        os.rename(r""+complete_name_file,r""+new_name_file)

def edit_selection(line_data):
    pos=5
    x = None
    h = curses.color_pair(1)
    n = curses.A_NORMAL
    while x != ord('\n'):
        print_card(line_data,"Que te gustaria editar?")
        display_titles_Editmenu(n)
        s = Higlight_Text_EditMenu()
        s.indirect(pos-4,h)
        screen.refresh()
        x = screen.getch()
        pos = move_button(x,pos,5,9)
    return ord(str(pos))

def display_titles_Editmenu(n):
    screen.addstr(9,4,"Nombre", n)
    screen.addstr(10,4,"Ataque", n)
    screen.addstr(11,4,"Defensa", n)
    screen.addstr(12,4,"Nivel Estrellas", n)
    screen.addstr(13,4,"Regresar", n)

class Higlight_Text_EditMenu(object):
    def indirect(self,i,h):
        method_name='number_'+str(i)
        method = getattr(self,method_name,lambda : 'Invalid')
        return method(h)
    def number_1(self,h):
        screen.addstr(9,4,"Nombre", h)
    def number_2(self,h):
        screen.addstr(10,4,"Ataque", h)
    def number_3(self,h):
        screen.addstr(11,4,"Defensa", h)
    def number_4(self,h):
        screen.addstr(12,4,"Nivel Estrellas", h)
    def number_5(self,h):
        screen.addstr(13,4,"Regresar", h)          
    
def eliminate(id,line_data,complete_name_file):
    if(id==1):
        with open(complete_name_file,'r') as f:
            f_lines = f.readlines()
        with open(complete_name_file,'w+') as f:
            for l in f_lines:
                line_data2 = l.split(',')
                if(line_data[0]!=line_data2[0]):
                    f.write(l)
            f.close()
    if(id==2):
        os.remove(complete_name_file)
   
def input():
    editwin = curses.newwin(1,60, 7,3)
    rectangle(screen, 6,2, 6+1+1, 2+60+1)
    screen.refresh()
    box = Textbox(editwin)
    box.edit()
    return box.gather()
    
def validate_type_card_name(name):
    new_file_name = name+".txt"
    for file in os.listdir("./CardTypes/"):
        if(file.lower()==new_file_name.lower()):
            return False
    return True

def print_card(card_data,complemento):
    screen.keypad(1)
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_YELLOW)
    title_deployment("Datos de la carta, "+complemento)
    screen.addstr(5,4,"Nombre: "+card_data[0], curses.A_BOLD)
    screen.addstr(6,4,"Nivel Estrellas: "+card_data[3], curses.A_BOLD)
    screen.addstr(7,4,"ATK: "+card_data[1], curses.A_BOLD)
    screen.addstr(8,4,"DEF: "+card_data[2], curses.A_BOLD)

def print_type_card(f_lines,complemento):
    screen.keypad(1)
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_YELLOW)
    title_deployment("Datos de la carta, "+complemento)
    i = 5
    for l in f_lines:
        card_data = l.split(',')
        screen.addstr(i,4,"Nombre: "+card_data[0], curses.A_BOLD)
        screen.addstr(i+1,4,"Nivel Estrellas: "+card_data[3], curses.A_BOLD)
        screen.addstr(i+2,4,"ATK: "+card_data[1], curses.A_BOLD)
        screen.addstr(i+3,4,"DEF: "+card_data[2], curses.A_BOLD)
        i = i+4
    return i

def edit_eliminate_selection2(line_data,flag):
    pos = 1
    aux = 0
    x = None
    h = curses.color_pair(1)
    n = curses.A_NORMAL
    while x != ord('\n'):
        min = print_type_card(line_data,"Que te gustaria hacer")
        if(flag):
            pos = min-4
            aux = min-4
            rest = aux*(aux-1)/aux
            display_titles_menu(n,"1 - Editar","2 - Eliminar","3 - Regresar",min,min+1,min+2)
            s = Higlight_Text_Menu()
            s.indirect(int(pos-rest),h,"1 - Editar","2 - Eliminar","3 - Regresar",min,min+1,min+2)
            screen.refresh()
            x = screen.getch()
            pos = move_button(x,pos,min-4,min+2)
            flag = False
        else:
            display_titles_menu(n,"1 - Editar","2 - Eliminar","3 - Regresar",min,min+1,min+2)
            s = Higlight_Text_Menu()
            s.indirect(int(pos-rest),h,"1 - Editar","2 - Eliminar","3 - Regresar",min,min+1,min+2)
            screen.refresh()
            x = screen.getch()
            pos = move_button(x,pos,aux,aux+2)
    if(pos==aux):
        return 5
    elif(pos==aux+1):
        return 6
    elif(pos==aux+2):
        return 7
    return 7

def edit_eliminate_selection1(line_data):
    pos = 5
    x = None
    h = curses.color_pair(1)
    n = curses.A_NORMAL
    while x != ord('\n'):
        print_card(line_data,"Que te gustaria hacer")
        display_titles_menu(n,"1 - Editar","2 - Eliminar","3 - Regresar",9,10,11)
        s = Higlight_Text_Menu()
        s.indirect(pos-4,h,"1 - Editar","2 - Eliminar","3 - Regresar",9,10,11)
        screen.refresh()
        x = screen.getch()
        pos = move_button(x,pos,5,7)
    return ord(str(pos))
    
def error_message(id,eror_message_id):
    pass
    
def main():
    getin = None 
    sub1get = None 
    while getin != ord('3'): 
        getin = topmenu() 
        if getin == ord('1'):
            sub_menu(sub1get=1,subtitle='CARTA')
            sub1get = None
        elif getin == ord('2'): 
            sub_menu(sub1get=2,subtitle='TIPO DE CARTA')
            sub1get = None
        elif getin == ord('3'): 
            curses.endwin()

if __name__ == "__main__":
    main()