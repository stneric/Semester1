################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/C\ Test\ 1\ Vorbereitung.c 

OBJS += \
./src/C\ Test\ 1\ Vorbereitung.o 

C_DEPS += \
./src/C\ Test\ 1\ Vorbereitung.d 


# Each subdirectory must supply rules for building sources it contributes
src/C\ Test\ 1\ Vorbereitung.o: ../src/C\ Test\ 1\ Vorbereitung.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/C Test 1 Vorbereitung.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


