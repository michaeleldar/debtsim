if [ $1="flags" ]; then
    python3.11 gen3.py
    python3.11 gen4.py
    python3.11 download.py
else
    echo "option not recognized"
fi
