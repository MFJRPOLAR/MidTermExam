class time:
    """The time class stores general information about a time.
    """    
    def __init__(self, hour: int, minute: int, second: int):
        """Constructs a time object having the specified hour, minute, and second, 
        and universal time in the format HH:MM:SS.

        :ivar __hour: hour of this time object
        :ivar __minute: minute of this time object
        :ivar __second: second of this time object
        :ivar __time: universal time of this time object in the format HH:MM:SS

        Args:
            hour (int): specified hour
            minute (int): specified minute
            second (int): specified second
    
        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
            ValueError: indicates specified minute is less than 0 or greater than 60
            ValueError: indicates specified second is less than 0 or greater than 60
        """   
        try: 
            if not isinstance(hour,int):
                raise ValueError("Hour is not a integer")
            elif hour > 24 or hour < 0: 
                raise ValueError("Hour is less than 0 or greater than 24")
            elif not isinstance(minute,int):
                raise ValueError("Minute is not a integer")
            elif minute > 60 or hour < 0: 
                raise ValueError("Minute is less than 0 or greater than 60")
            elif not isinstance(second,int):
                raise ValueError("Second is not a integer")
            elif second > 60 or second < 0: 
                raise ValueError("Second is less than 0 or greater than 60")
        except ValueError as e: 
            exit(e)
        finally:
            self.__hour = hour
            self.__minute = minute
            self.__second = second
            self.__time = f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
             

    def getHour(self):
        """Returns the hour of the calling time object.

        Returns:
            int: hour of the calling time object
        """ 
        return self.__hour
    
    def setHour(self, hour: int):
        """Sets the hour of the calling time object to the specified hour and
        recomputes the universal time of the calling time object.

        Args:
            hour (int): specified hour

        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
        """        
        try: 
            if not isinstance(hour,int):
                raise ValueError("Hour is not a integer")
            elif hour > 24 or hour < 0: 
                raise ValueError("Hour is less than 0 or greater than 24")
        except ValueError as e: 
            exit(e)
        finally: 
            self.__hour = hour 
            self.__time = f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def getMinute(self):
        """Returns the minute of the calling time object.

        Returns:
            int: minute of the calling time object
        """ 
        return self.__minute
    
    def setMinute(self, minute: int):
        """Sets the minute of the calling time object to the specified minute and
        recomputes the universal time of the calling time object.

        Args:
            minute (int): specified minute

        Raises:
            ValueError: indicates specified minute is less than 0 or greater than 60
        """
        try: 
            if not isinstance(minute,int):
                raise ValueError("Minute is not a integer")
            elif minute > 60 or minute < 0: 
                raise ValueError("Minute is less than 0 or greater than 60")
        except ValueError as e: 
            exit(e)
        finally: 
            self.__minute = minute
            self.__time = f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def getSecond(self):
        """Returns the second of the calling time object.

        Returns:
            int: second of the calling time object
        """
        return self.__second
    
    def setSecond(self, second: int):
        """Sets the second of the calling time object to the specified second and
        recomputes the universal time of the calling time object.

        Args:
            second (int): specified second

        Raises:
            ValueError: indicates specified second is less than 0 or greater than 60
        """
        try: 
            if not isinstance(second,int):
                raise ValueError("Second is not a integer")
            elif second > 60 or second < 0: 
                raise ValueError("Second is less than 0 or greater than 60")
        except ValueError as e: 
            exit(e)
        finally: 
            self.__second = second
            self.__time = f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def getTime(self):
        """Returns the universal time of the calling time object.

        Returns:
            str: universal time of the calling time object
        """
        return self.__time 
    
    def __str__(self):
        """Returns string representation of the calling time object.

        Returns:
            str: string representation of the calling time object
        """  
        return f"time={self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"     
    
    def __eq__(self, other):
        """Tests if the calling time object is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling time object is equal to the specified
            object, else False
        """
        if isinstance(other,time):
            if other.__hour == self.__hour:
                if other.__minute == self.__minute:
                    if other.__second == self.__second:
                        if other.__time == self.__time:
                            return True
        return False
    
    @staticmethod
    def sort(data, first: int, last: int):
        """Sorts a list from smallest to largest using the insertion sort
        algorithm bypassing the elements to the left of first and to the
        right of last.

        Args:
            data: list to sort
            first (int): list index at which the sort will begin
            last (int): list index at which the sort will end
        """  
        # Initialize loop counter variable i to 1 
        i = 1 

        # Initialize loop counter variable j to 0 
        j  = 0 

        # Initialize next value to 0 
        nextVal = 0 

        # loop through list as many times as specified by the
        # length of the list and first 
        # this loop represents the blue arrow 
        while(i <= last):
            # store a copy of the number in index position first + i 
            # in next value  
            nextVal = data[first+i]

            # loop through the list starting at the same index as 
            # next value and iterate back toward first as long as 
            # the element to the left of next value is greater than 
            # next value and we're not the whole way back to first 
            j = first + i 
            while (j > first and data[j-1]> nextVal):
                # shift the element to left of next value right
                # ward one position 
                data[j] = data[j-1]

                # insert next value into the element that was just 
                # shifted 
                data[j-1] = nextVal 

                # decrement j by 1 
                j -= 1 

            # increment i by 1 
            i += 1 
    

    @staticmethod
    def search (a, first: int, last: int, target: int):
        """Searches part of a sorted list for a specified target starting at a[first]
        and ending at a[last].

        Args:
            a (int): the list to search
            first (int): the list index at which the search will start
            last (int): the list index at which the search will end
            target (int): the element to search for

        Returns:
            int: If target appears in the list, index of the, element 
            that contains target; else -1.
        """
        # set a boolean variable found to false 
        found = False

        # set an int variable size to list length - first
        size = len(a) - first 

        # set an int variable middle to first + size / 2 
        middle = int(first + (size / 2))

        # if there are no more elements to search 
        if (size <= 0): 
            return  -1 
        else:
            # while there are more elements to search and 
            # the target hasn't been found 
            while (size > 0 and not found):
                # if the value in the middle element is the target 
                if (a[middle]==target):
                    found = True 
                elif (a[middle] > target):
                    # else if the value in the middle element is 
                    # greater than the target
                    size  = int(size / 2)
                else:
                    # else if the value in the middle element is 
                    # less than the target 
                    first = middle + 1 
                    size = int((size-1)/2)

                # recompute middle 
                middle = int(first + size/2)

        # check if the target was found 
        if (found):
            return middle 
        else:
            return -1 

            