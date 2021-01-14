
def create_beat_distribution(dist):
    assert (len(dist) == 8), "8 numbers required"
    result = {} 
    for i in range(-4, 3, 1):
        result[beat * (2**i)] = dist[i+4]
    return result

def create_note_distribution(dist):
    assert (len(dist) == 8), "8 numbers required"
    return list(result)



beat = 480 #common number of beats per quarter

sample_distributions = {
    #"default" : create_beat_distribution([0, 0, 1, 8, 16, 5, 3, 2]),
    "slow" : create_beat_distribution([0, 0, 0, 0, 0, 3, 3, 6])
}
print(sample_distributions["slow"])

"""
beat / 16 : 0,    #
beat / 8  : 0,    #
beat / 4  : 1,    # 16th note
beat / 2  : 8,    # Eight note
beat / 1  : 16,   # Quarter in /4 time sig
beat * 2  : 5,    # Half Note
beat * 3  : 3,    # Dotted half 
beat * 4  : 2     # Whole note
"""

instruments = {
    "piano": {
        "acoustic grand piano" : 0x00,
        "bright acoustic piano" : 0x01,
        "electric grand piano" : 0x02,
        "honky tonk piano" : 0x03,
        "electric piano 1" : 0x04,
        "electric piano 2" : 0x05,
        "harpsicord" : 0x06,
        "clavinet" : 0x07

    },
    "chromatic percussion" : {
        "celesta" : 0x08,
        "glockenspiel" : 0x09,
        "music box" : 0x0a,
        "vibraphone" : 0x0b,
        "marimba" : 0x0c,
        "xylophone" : 0x0d,
        "tubular bell" : 0x0e,
        "dulcimer" : 0x0f
    },
    "organ" : {
        "hammond / drawbar organ" : 0x10,
        "percussive organ" : 0x11,
        "rock organ" : 0x12,
        "church organ" : 0x13,
        "reed organ" : 0x14,
        "accordion" : 0x15,
        "harmonica" : 0x16,
        "tango accordion" : 0x17
    },
    "guitar" : {
            
        "nylon string acoustic guitar" : 0x18,
        "steel string acoustic guitar" : 0x19,
        "jazz electric guitar" : 0x1a,
        "clean electric guitar" : 0x1b,
        "muted electric guitar" : 0x1c,
        "overdriven guitar" : 0x1d,
        "distortion guitar" : 0x1e,
        "guitar harmonics" : 0x1f
    },
    "bass" : {
        "acoustic bass" : 0x20,
        "fingered electric bass" : 0x21,
        "picked electric bass" : 0x22,
        "fretless bass" : 0x23,
        "slap bass 1" : 0x24,
        "slap bass 2" : 0x25,
        "synth bass 1" : 0x26,
        "synth bass 2" : 0x27
    },
    "strings" : {
        "violin" : 0x28,
        "viola" : 0x29,
        "cello" : 0x2a,
        "contrabass" : 0x2b,
        "tremolo strings" : 0x2c,
        "pizzicato strings" : 0x2d,
        "orchestral strings / harp" : 0x2e,
        "timpani" : 0x2f
    },
    "ensemble" : {
        "string ensemble 1" : 0x30,
        "string ensemble 2 / slow strings" : 0x31,
        "synth strings 1" : 0x32,
        "synth strings 2" : 0x33,
        "choir aahs" : 0x34,
        "voice oohs" : 0x35,
        "synth choir / voice" : 0x36,
        "orchestra hit" : 0x37,
    },
    "brass" : {
        "trumpet" : 0x38,
        "trombone" : 0x39,
        "tuba" : 0x3a,
        "muted trumpet" : 0x3b,
        "french horn" : 0x3c,
        "brass ensemble" : 0x3d,
        "synth brass 1" : 0x3e,
        "synth brass 2" : 0x3f,
    },
    "reed" : {  
        "soprano sax" : 0x40,
        "alto sax" : 0x41,
        "tenor sax" : 0x42,
        "baritone sax" : 0x43,
        "oboe" : 0x44,
        "english horn" : 0x45,
        "bassoon" : 0x46,
        "clarinet" : 0x47
    },
    "pipe" : {    
        "piccolo" : 0x48,
        "flute" : 0x49,
        "recorder" : 0x4a,
        "pan flute" : 0x4b,
        "bottle blow / blown bottle" : 0x4c,
        "shakuhachi" : 0x4d,
        "whistle" : 0x4e,
        "ocarina" : 0x4f
    },
    "synth lead" : {
        "synth square wave" : 0x50,
        "synth saw wave" : 0x51,
        "synth calliope" : 0x52,
        "synth chiff" : 0x53,
        "synth charang" : 0x54,
        "synth voice" : 0x55,
        "synth fifths saw" : 0x56,
        "synth brass and lead" : 0x57,
    },
    "synth pad" : {
        "fantasia / new age" : 0x58,
        "warm pad" : 0x59,
        "polysynth" : 0x5a,
        "space vox / choir" : 0x5b,
        "bowed glass" : 0x5c,
        "metal pad" : 0x5d,
        "halo pad" : 0x5e,
        "sweep pad" : 0x5f
    },
    "synth effects" : {
        "ice rain" : 0x60,
        "soundtrack" : 0x61,
        "crystal" : 0x62,
        "atmosphere" : 0x63,
        "brightness" : 0x64,
        "goblins" : 0x65,
        "echo drops / echoes" : 0x66,
        "sci fi" : 0x67
    },
    "ethnic" : {
        "sitar" : 0x68,
        "banjo" : 0x69,
        "shamisen" : 0x6a,
        "koto" : 0x6b,
        "kalimba" : 0x6c,
        "bag pipe" : 0x6d,
        "fiddle" : 0x6e,
        "shanai" : 0x6f,
    },
    "percussive" : {
        "tinkle bell" : 0x70,
        "agogo" : 0x71,
        "steel drums" : 0x72,
        "woodblock" : 0x73,
        "taiko drum" : 0x74,
        "melodic tom" : 0x75,
        "synth drum" : 0x76,
        "reverse cymbal" : 0x77
    },
    "sound effects" : {   
        "guitar fret noise" : 0x78,
        "breath noise" : 0x79,
        "seashore" : 0x7a,
        "bird tweet" : 0x7b,
        "telephone ring" : 0x7c,
        "helicopter" : 0x7d,
        "applause" : 0x7e,
        "gunshot" : 0x7f
    }

}
