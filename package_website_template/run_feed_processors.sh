#!/bin/bash

PRIVATEPROPERTY=`find . -name 'PrivateProperty-*.jar' | sed 's/^\.\///g' | sort -V | tail -n 1`
PROPERTY24=`find . -name 'Property24-*.jar' | sed 's/^\.\///g' | sort -V | tail -n 1`
PROPERTYGENIE=`find . -name 'PropertyGenie-*.jar' | sed 's/^\.\///g' | sort -V | tail -n 1`
SAHOMETRADERS=`find . -name 'SaHometraders-*.jar' | sed 's/^\.\///g' | sort -V | tail -n 1`

if [ x"$PRIVATEPROPERTY" != x"" ]; then
    java -Dlog4j.configuration="file://`pwd`/privateproperty.log4j.properties" -jar $PRIVATEPROPERTY
fi

if [ x"$PROPERTYGENIE" != x"" ]; then
    java -Dlog4j.configuration="file://`pwd`/propertygenie.log4j.properties" -jar $PROPERTYGENIE
fi

if [ x"$PROPERTY24" != x"" ]; then
    java -Dlog4j.configuration="file://`pwd`/property24.log4j.properties" -jar $PROPERTY24
fi

if [ x"$SAHOMETRADERS" != x"" ]; then
    java -Dlog4j.configuration="file://`pwd`/sahometraders.log4j.properties" -jar $SAHOMETRADERS
fi
