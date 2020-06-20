html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                sum : <input type="number" name="a" >
                    + <input type="number" name="b" >
            </p>
            <p>
                prod : <input type="number" name="a">
                     x <input type="number" name="b">
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

