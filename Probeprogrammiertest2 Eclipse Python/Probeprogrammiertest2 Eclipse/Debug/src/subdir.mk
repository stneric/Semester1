################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/Probeprogrammiertest2\ Eclipse.c 

OBJS += \
./src/Probeprogrammiertest2\ Eclipse.o 

C_DEPS += \
./src/Probeprogrammiertest2\ Eclipse.d 


# Each subdirectory must supply rules for building sources it contributes
src/Probeprogrammiertest2\ Eclipse.o: ../src/Probeprogrammiertest2\ Eclipse.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"src/Probeprogrammiertest2 Eclipse.d" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


