<?php 
# should not report missing doc comments
# should report Unnecessary FINAL modifier in FINAL class
final class SomeClass
{
    public final function SomeMethod()
    {
    }
}
?>