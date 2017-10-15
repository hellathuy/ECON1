#include <stdio.h>
#include <stdlib.h>

void PED();
void PES();
void IED();
void CPED();

int Q1; //beginning quantity
int Q2; //new quantity
int S1; //beginning supply
int S2; //new supply
float P1; //beginning price
float P2; //new price
float I1; //beginning income
float I2; //new income

int main() {
	printf("Good day, Thuy.\nAll calculations made will be using the midpoint method.");

	while (1) {
		int option;
		printf("\nWhat would you like to calculate? (To quit program, press CTRL + C.)\n\t1. calculate the price elasticity of demand\n\t2. calculate the price elasticity of supply\n\t3. calculate the income elasticity of demand\n\t4. calculate the cross-price elasticity of demand\n");
		scanf("%d", &option);

	switch(option) {
		case '1':
			PED();
			break;

		case '2':
			PES();
			break;

		case '3':
			IED();
			break;

		case '4':
			CPED();
			break;

		default:
			printf("Please input a valid option.");
		}
	}
}

void PED() {
	float percentageChangeQD;
	float percentageChangeP;
	float PED;

	printf("CALCULATING PRICE ELASTICITY OF DEMAND:\n");

	//receiving input values
	printf("What is the initial quantity demanded? ");
	scanf("%d", &Q1);

	printf("\nWhat is the new quantity demanded? ");
	scanf("%d", &Q2);

	printf("\nWhat is the initial price? ");
	scanf("%f", &P1);

	printf("\nWhat is the new price? ");
	scanf("%f", &P2);

	//calculating percentage change in quantity demanded
	percentageChangeQD = (Q2 - Q1)/((Q2 + Q1)/2);

	//calculating percentage change in price
	percentageChangeP = (P2 - P1)/((P2 + P1)/2);

	//calculating PED
	PED = percentageChangeQD / percentageChangeP;

	printf("\nPercentage Change in Quantity Demanded: %.2f", percentageChangeQD);
	printf("\nPercentage Change in Price: %.2f", percentageChangeP);
	printf("\nPrice Elasticity of Demand: %.2f", PED);

}

void PES() {
	float percentageChangeQS;
	float percentageChangeP;
	float PES;

	printf("CALCULATING PRICE ELASTICITY OF SUPPLY:\n");

	//receiving input values
	printf("What is the initial quantity supplied? ");
	scanf("%d", &Q1);

	printf("\nWhat is the new quantity supplied? ");
	scanf("%d", &Q2);

	printf("\nWhat is the initial price? ");
	scanf("%f", &P1);

	printf("\nWhat is the new price? ");
	scanf("%f", &P2);

	//calculating percentage change in quantity supplied
	percentageChangeQS = (Q2 - Q1)/((Q2 + Q1)/2);

	//calculating percentage change in price
	percentageChangeP = (P2 - P1)/((P2 + P1)/2);

	//calculating PES
	PES = percentageChangeQS / percentageChangeP;

	printf("\nPercentage Change in Quantity Supplied: %.2f", percentageChangeQS);
	printf("\nPercentage Change in Price: %.2f", percentageChangeP);
	printf("\nPrice Elasticity of Supply: %.2f", PES);

}

void IED() {
	float percentageChangeQD;
	float percentageChangeI;
	float IED;

	printf("CALCULATING INCOME ELASTICITY OF DEMAND:\n");

	//receiving input values
	printf("What is the initial quanity demanded? ");
	scanf("%d", &Q1);

	printf("\nWhat is the new quantity demanded? ");
	scanf("%d", &Q2);

	printf("\nWhat is the initial income? ");
	scanf("%f", &I1);

	printf("\nWhat is the new income? ");
	scanf("%f", &I2);

	//calculating percentage change in quantity demanded
	percentageChangeQD = (Q2 - Q1)/((Q2 + Q1)/2);

	//calculating percentage change in income
	percentageChangeI = (I2 - I1)/((I2 + I1)/2);

	//calculating IED
	IED = percentageChangeQD / percentageChangeI;

	printf("\nPercentage Change in Quantity Demanded: %.2f", percentageChangeQD);
	printf("\nPercentage Change in Income: %.2f", percentageChangeI);
	printf("\nIncome Elasticity of Demand: %.2f", IED);

}

void CPED() {
	float percentageChangeQD;
	float percentageChangeP;
	float CPED;

	printf("CALCULATING CROSS-PRICE ELASTICITY OF DEMAND:\n");

	//receiving input values
	printf("What is the initial quantity demanded of Good 1? ");
	scanf("%d", &Q1);

	printf("\nWhat is the new quantity demanded of Good 1? ");
	scanf("%d", &Q2);

	printf("\nWhat is the initial price of Good 2? ");
	scanf("%f", &P1);

	printf("\nWhat is the new price of Good 2? ");
	scanf("%f", &P2);

	//calculating percentage change in quantity supplied
	percentageChangeQD = (Q2 - Q1)/((Q2 + Q1)/2);

	//calculating percentage change in price
	percentageChangeP = (P2 - P1)/((P2 + P1)/2);

	//calculating PES
	CPED = percentageChangeQD / percentageChangeP;

	printf("\nPercentage Change in Quantity Demanded of Good 1: %.2f", percentageChangeQD);
	printf("\nPercentage Change in Price of Good 2: %.2f", percentageChangeP);
	printf("\nCross-Price Elasticity of Demand: %.2f", CPED);

}
