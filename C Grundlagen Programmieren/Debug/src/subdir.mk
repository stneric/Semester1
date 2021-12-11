################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/C\ Grundlagen\ Programmieren.c 

OBJS += \
./src/C\ Grundlagen\ Programmieren.o 

C_DEPS += \
./src/C\ Grundlagen\ Programmieren.d 


# Each subdirectory must supply rules for building sources it contributes
src/C\ Grundlagen\ Programmieren.o: ../src/C\ Grundlagen\ Programmieren.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/C Grundlagen Programmieren.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


