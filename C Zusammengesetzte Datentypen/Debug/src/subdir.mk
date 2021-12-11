################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/C\ Zusammengesetzte\ Datentypen.c 

OBJS += \
./src/C\ Zusammengesetzte\ Datentypen.o 

C_DEPS += \
./src/C\ Zusammengesetzte\ Datentypen.d 


# Each subdirectory must supply rules for building sources it contributes
src/C\ Zusammengesetzte\ Datentypen.o: ../src/C\ Zusammengesetzte\ Datentypen.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/C Zusammengesetzte Datentypen.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


