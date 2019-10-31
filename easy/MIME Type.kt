import java.util.*
import java.io.*
import java.math.*

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val N = input.nextInt() // Number of elements which make up the association table.
    val Q = input.nextInt() // Number Q of file names to be analyzed.
    val extToMt:HashMap<String,String> = HashMap<String,String>()
    for (i in 0 until N) {
        val EXT = input.next() // file extension
        val MT = input.next() // MIME type.
        extToMt.put(EXT, MT)
    }
    input.nextLine()
    for (i in 0 until Q) {
        val FNAME = input.nextLine() // One file name per line.
        var mt : String? = "UNKNOWN"
        /**
    if '.'  in fname:
        ext = fname.split('.')[len(fname.split('.'))-1].lower()
        if ext in ext_to_mt:
            mt =  ext_to_mt[ext] 
    print(mt)
        */
        if(FNAME.contains('.') && FNAME.split('.').size > 1) {
            val EXT : String = FNAME.split('.')[FNAME.split('.').size-1].toLowerCase()
            if(extToMt.contains(EXT)) {
                mt = extToMt.get(EXT)
            }
        }

    }

    // Write an action using println()
    // To debug: System.err.println("Debug messages...");


    // For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
    println("UNKNOWN")
}