html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                first number : <input type="number" name="a" >
            </p>
            <p>
                second number : <input type="number" name="b">
            </p>
            <p>
            <input type="submit" value="Submit">
            </p>
        </form>
        <p>
           sum= %(sum)s</br>
           prod= %(prod)s</br>
        </p>
    </body>
</html>
"""

