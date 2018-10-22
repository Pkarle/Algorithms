# -*- coding: utf-8 -*-
import random
# @author Alexandre Benoit, LISTIC Lab, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management

def average_above_zero(tab):
    """
    brief: computes teh average of ...
    Args:
        tab: a list of numeric value
    Return: 
        The computed average
    Raises:
        ValueError if no positive value is found
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    average = -99
    valSum = 0.0
    nPositiveValues = 0
    NMAX = len(tab)
    for idx in range(NMAX):
        if tab[idx] > 0:
            valSum = valSum + float(tab[idx])
            nPositiveValues = nPositiveValues + 1

    if nPositiveValues <= 0:
        raise(ValueError('No positive value found'))
    average = valSum / nPositiveValues
    return average

tab = [1, 2, 3, 4, -5]
moy = average_above_zero(tab)
print('Positive values average = ' + str(moy))
print('Positive values average = '.format(v=moy))

def max_value(input_list):
    """
    brief: return the maxValue and the index of this a value of a given list
    Args:
        @param input_list : the input list to be scanned
    Raises:
        throws an exception (ValueError) when the list is empty
    Return: The maxValue of a List and the index
    """

    if not(isinstance(input_list, list)):
        raise ValueError('The parameter given is not type of list')
    maxVal = 0
    maxIndex = 0
    for idx in range(len(input_list)):
        if maxVal < input_list[idx]:
            maxVal = input_list[idx]
            maxIndex = input_list.index(input_list[idx])
    if maxVal == 0:
        raise ValueError('None of the value in this list are higher than 0')
    return maxVal, maxIndex

maxList = [1, 203, 40, 50]

print('The entire list of number : ' + str(maxList))
print('The max value of this list equal to : ' + str(max_value(maxList)))

def reverse_table(tableList):
    """
    brief: Reverse value in a given list
    Args:
        @param tableList : the table list to be scanned
    Raises:
        throws an exception (ValueError) when the list is empty
    Return: Return the reversed array
    """

    if not tableList:
        raise ValueError('Empty list given')

    for idx in range(len(tableList)):
        currentValue = tableList[idx]
        currentIndex = tableList.index(currentValue)
        
        tableList.pop(currentIndex)
        tableList.insert(0, currentValue)
    
    return tableList

reverseList = [20, 50, 60, 80]
print('The initial list : ' + str(reverseList))
print('The reversed list : ' + str(reverse_table(reverseList)))


def remove_whitespace(tableString):
    """
    brief: Remove whitespace in a given string
    Args:
        @param tableString : the string that has to be scanned
    Raises:
        throws an exception (ValueError) when the value is not type of string
    Return: Return the string without space
    """

    if isinstance(tableString, int):
        raise ValueError('The given value is not of type string')

    tableString = tableString.replace(" ", "")

    return tableString

sentence = 'My name is '
print('The initial string: ' + str(sentence))
print('The string whith no whitespace : ' + remove_whitespace(sentence))

def shuffle(list):
    shuffledList = []
    while len(shuffledList) != len(list):
        randomIndex = random.randint(0, len(list) - 1)
        currentValue = list[randomIndex]
        if currentValue not in shuffledList:
            shuffledList.insert(0, currentValue)
    return shuffledList

shuffleList = [10, 20, 8, 5, 50]
print('The shuffled list : ' + str(shuffle(shuffleList)))
# The function is not working yet