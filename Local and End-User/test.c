/*
 * Farm.c
 *
 * Created: 1/14/2016 12:14:06 AM
 *  Author: Thuong
 */ 

#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>
#include "./LCD/lcd.h"
#include "Timer/timer.h"
//#include "./Ex Interrupt/ExInterrupt.h"
//#include "./Uart/uart.h"
#include "Input/input.h"

#define FOSC 8000000
#define BAUD 9600
#define UBRR ((FOSC/(16*BAUD))-1)
unsigned char Uart_rev = 0;

void UART_init()
{
	/* Set baud rate */
	
	UBRRH= 0x00;
	UBRRL= 0x33;
	
	UCSRA=0X00;
	/* Enable receiver and transmitter */
	UCSRB=(1<<TXEN)|(1<<RXEN)|(1<<RXCIE); // '(1<<RXCIE)' enable interrupt
	/* Set frame format: 8data, 1stop bit */
	UCSRC=(1<<URSEL)|(1<<UCSZ1)|(1<<UCSZ0);
	//UCSRC = (1 << USBS) | (3 << UCSZ0);
	//UCSRC = 0b00000110;
	//UCSRC=(1<<UCSZ1)|(1<<UCSZ0);
	sei(); // enable global interrupt
}

void USART_Transmit( unsigned char data )
{
	/* Wait for empty transmit buffer */
	while ( !(UCSRA & (1<<UDRE)) );
	/* Put data into buffer, sends the data */
	UDR = data;
}

unsigned char USART_Receive( void )
{
	/* Wait for data to be received */
	while ( !(UCSRA & (1<<RXC)) );
	/* Get and return received data from buffer */
	return UDR;
}
ISR (USART_RXC_vect)
{
	Uart_rev = USART_Receive();
	lcd_set_cursor(0,0);
	//USART_Transmit('1');
	lcd_write_character_4d(Uart_rev);

}
void init_system(void)
{

	//init_timer0(154);	// Timer0 5ms
	//SetTimer0_ms(200);	// Cycles 10ms
	//
	//init_timer1(49000);	// Timer 50ms
	//SetTimer1_ms(10);	// Cycles 500ms
	lcd_init_4d();
	UART_init();
	//init_input();
	_delay_ms(1000);
}

int main(void)
{
	init_system();
	while(1)
	{
		
		
	}
	return 0;
}


