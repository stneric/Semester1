################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/Rekursion\ Wiederholung.c 

OBJS += \
./src/Rekursion\ Wiederholung.o 

C_DEPS += \
./src/Rekursion\ Wiederholung.d 


# Each subdirectory must supply rules for building sources it contributes
src/Rekursion\ Wiederholung.o: ../src/Rekursion\ Wiederholung.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/Rekursion Wiederholung.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


