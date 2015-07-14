# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from random import randint

LADO_CADRADO = 35
LADO_VENTANA = LADO_CADRADO * 9

lista_numeros = []

for i in range(81):
	lista_numeros.append(0)
	
lista_editados = []

for i in range(81):
	lista_editados.append(False)
	
casilla_seleccionada = -1

#FUNCIONS PARA RESOLVER O SUDOKU:

#COMPROBAR SE A FILA ESTA BEN:

#lista + int + int -> bool

def comp_fila(lista,fila,final=False,lista_e=False):
	salida = True
	lista_salida = []
	if lista_e:
		lista_edit = []
	if not final:
		rango = fila*9+9
	else:
		rango = final
	for i in range(fila*9,rango,1):
		if lista[i] == 0:
			salida = False
		lista_salida.append(lista[i])
		if lista_e and lista_e[i]:
			lista_edit.append(lista[i])
	if len(set(lista_salida)) < len(lista_salida):
		salida = False
	if not lista_e:
		return salida
	else:
		return lista_edit

#COMPROBAR SE A COLUMNA ESTA BEN:

#lista + int + int -> bool
	
def comp_colum(lista,columna,final=False,lista_e=False):
	salida = True
	lista_salida = []
	if lista_e:
		lista_edit = []
	if not final:
		rango = 72+columna+1
	else:
		rango = final
	for i in range(columna,rango,9):
		if lista[i] == 0:
			salida = False
		lista_salida.append(lista[i])
		if lista_e and lista_e[i]:
			lista_edit.append(lista[i])
	if len(set(lista_salida)) < len(lista_salida):
		salida = False
	if not lista_e:
		return salida
	else:
		return lista_edit

#COMPROBAR SE O CADRO(GROSO) ESTA BEN:

#lista + int + int -> bool
	
def comp_cadro(lista,cadro,final=-1,lista_e=False):
	salida = True
	lista_salida = []
	if lista_e:
		lista_edit = []
	
	if cadro > 5:
		indice = (cadro-6)*3+(cadro/3)*27
	elif cadro > 2:
		indice = (cadro-3)*3+(cadro/3)*27
	else:
		indice = cadro*3+(cadro/3)*27
		
	if cadro > 5:
		rango1 = (cadro-6)*3+(cadro/3)*27+3
		rango2 = (cadro-6)*3+(cadro/3)*27+3+9
		rango3 = (cadro-6)*3+(cadro/3)*27+3+18
		if final >= 0:
			rango = final
		else:
			rango = rango3
	elif cadro > 2:
		rango1 = (cadro-3)*3+(cadro/3)*27+3
		rango2 = (cadro-3)*3+(cadro/3)*27+3+9
		rango3 = (cadro-3)*3+(cadro/3)*27+3+18
		if final >= 0:
			rango = final
		else:
			rango = rango3
	else:
		rango1 = cadro*3+(cadro/3)*27+3
		rango2 = cadro*3+(cadro/3)*27+3+9
		rango3 = cadro*3+(cadro/3)*27+3+18
		if final >= 0:
			rango = final 
		else:
			rango = rango3
	
	for i in range(indice,rango1,1):
		if i <= rango:
			if lista[i] == 0:
				salida = False
			lista_salida.append(lista[i])
			if lista_e and lista_e[i]:
				lista_edit.append(lista[i])
			
	for i in range(indice+9,rango2,1):
		if i <= rango:
			if lista[i] == 0:
				salida = False
			lista_salida.append(lista[i])
			if lista_e and lista_e[i]:
				lista_edit.append(lista[i])
			
	for i in range(indice+18,rango3,1):
		if i <= rango:
			if lista[i] == 0:
				salida = False
			lista_salida.append(lista[i])
			if lista_e and lista_e[i]:
				lista_edit.append(lista[i])
			
	if len(set(lista_salida)) < len(lista_salida):
		salida = False
	if not lista_e:
		return salida
	else:
		return lista_edit

#CREAR LISTA ALEATORIA:

#lista[0,1,2,3,4,5,6,7,8] -> lista

def lista_aleatoria(lista):
	lista_final = []
	while len(lista) > 0:
		numero_aleatorio = randint(0,len(lista)-1)
		lista_final.append(lista[numero_aleatorio])
		del lista[numero_aleatorio]
		
	return lista_final
	
#QUITAR NUMEROS (XA POSTOS POLO USUARIO) DA LISTA:

#lista(editados) + lista + indice -> lista

def lista_postos(list_e, lista_n, indice):
	lista_salida =  lista_aleatoria([1,2,3,4,5,6,7,8,9])
	lista_del = comp_fila(lista_n,indice/9,lista_e=list_e) + comp_colum(lista_n,indice%9,lista_e=list_e) + comp_cadro(lista_n,cal_cadro(indice),lista_e=list_e)
	lista_del = set(lista_del)
	for i in lista_del:
		lista_salida.remove(i)
	return lista_salida
	
#SABER SI UN SUDOKU ESTA BEN:

def comp_sudoku(lista):
	salida = True
	for i in range(9):
		if not comp_fila(lista,i):
			salida = False
		if not comp_colum(lista,i):
			salida = False
		if not comp_cadro(lista,i):
			salida = False
	return salida

# CALCULAR CADRO

#int -> int	

def cal_cadro(n):
	if n in [0,1,2,9,10,11,18,19,20]:
		return 0
	elif n in [3,4,5,12,13,14,21,22,23]:
		return 1
	elif n in [6,7,8,15,16,17,24,25,26]:
		return 2
	elif n in [27,28,29,36,37,38,45,46,47]:
		return 3
	elif n in [30,31,32,39,40,41,48,49,50]:
		return 4
	elif n in [33,34,35,42,43,44,51,52,53]:
		return 5
	elif n in [54,55,56,63,64,65,72,73,74]:
		return 6
	elif n in [57,58,59,66,67,68,75,76,77]:
		return 7
	elif n in [60,61,62,69,70,71,78,79,80]:
		return 8
		
	
#RESOLVER SUDOKU

#lista + lista -> lista

def resolver_sudoku(lista, editados):
	lista_final = lista[:]
	while True:
		for i in range(81):
			reset = False
			l_aleatoria = lista_postos(lista_editados, lista, i)
			if not editados[i]:
				for x in l_aleatoria:
					lista_final[i] = x
					if comp_fila(lista_final,i/9,i+1) and comp_colum(lista_final,i%9,i+1) and comp_cadro(lista_final,cal_cadro(i),i):
						break
					if x == l_aleatoria[len(l_aleatoria)-1]:
						reset = True
			if reset == True:
				break
		break
	return lista_final
		
	
	

pygame.init()

ventana = pygame.display.set_mode([LADO_VENTANA, LADO_VENTANA])
pygame.display.set_caption("Resolvedor-Sudokus")

font = pygame.font.SysFont("Courier", LADO_CADRADO)

N_TICKS = 60

ON = True

Resolver = False

#BUCLE PYGAME

while ON:
	
	reloj = pygame.time.Clock()
	
	ventana.fill((255,255,255))
	
	#DEBUXAR CASILLA SELECCIONADA:
	
	if casilla_seleccionada >= 0:
		casilla_y = 0
		casilla_x = casilla_seleccionada
		while casilla_x >= 9:
			casilla_x -= 9
			casilla_y += 1
		rect_fondo = pygame.Rect(casilla_x*LADO_CADRADO, casilla_y*LADO_CADRADO, LADO_CADRADO, LADO_CADRADO)
		pygame.draw.rect(ventana, (200,200,200), rect_fondo)
	
	#DEBUXAR CADRICULA:
	
	saltos = 0
	for i in range(LADO_CADRADO,LADO_VENTANA,LADO_CADRADO):
		saltos += 1
		if saltos%3 == 0:
			grosor = 3
		else:
			grosor = 1
		pygame.draw.line(ventana, [0,0,0], [0, i], [LADO_VENTANA,i], grosor)
		pygame.draw.line(ventana, [0,0,0], [i,0], [i,LADO_VENTANA], grosor)
	
	#DEBUXAR NUMEROS:
	
	color_defecto = [0,0,0]
	indice_y = -LADO_CADRADO/20
	for i in range(9):
		for x in range(9):
			if lista_numeros[x+i*9] != 0:
				if lista_editados[x+i*9]:
					color_defecto = [100,0,0]
				else:
					color_defecto = [0,0,0]
				texto = font.render(str(lista_numeros[x+i*9]),True,color_defecto)
				ventana.blit(texto, [(x*LADO_CADRADO)+(LADO_CADRADO/5.8),indice_y+i*LADO_CADRADO])
				
	#RESOLUCIÓN
	
	if not comp_sudoku(lista_numeros) and Resolver:
		lista_numeros = resolver_sudoku(lista_numeros,lista_editados)
	if comp_sudoku(lista_numeros):
		Resolver = False
	if Resolver:
		N_TICKS = 500
	else:
		N_TICKS = 60
				
	#MOUSE
	
	if pygame.mouse.get_pressed()[0] == 1:
		p = pygame.mouse.get_pos()
		casilla_seleccionada = int(p[0]/LADO_CADRADO + (p[1]/LADO_CADRADO)*9)

	#TECLADO
	
	pygame.display.update()

	for evento in pygame.event.get():
		if evento.type == pygame.KEYDOWN:
			if evento.key == K_RETURN:
				if Resolver:
					Resolver = False
				else:
					Resolver = True
			if evento.key == K_DELETE:
				for i in range(81):
					lista_numeros[i] = 0
				for i in range(81):
					lista_editados[i] = False
			if casilla_seleccionada >= 0:
				if evento.key in [K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]:
					lista_numeros[casilla_seleccionada] = int(pygame.key.name(evento.key))
					if int(pygame.key.name(evento.key)) > 0:
						lista_editados[casilla_seleccionada] = True
					else:
						lista_editados[casilla_seleccionada] = False
		if evento.type == pygame.QUIT:
			pygame.display.quit()
			ON = False
	
	reloj.tick(N_TICKS)