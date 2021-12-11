################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/C\ Funktionen\ berechnen.c 

OBJS += \
./src/C\ Funktionen\ berechnen.o 

C_DEPS += \
./src/C\ Funktionen\ berechnen.d 


# Each subdirectory must supply rules for building sources it contributes
src/C\ Funktionen\ berechnen.o: ../src/C\ Funktionen\ berechnen.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/C Funktionen berechnen.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


