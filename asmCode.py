class Code(object):

    _comp_dict = {
        
            }
    _jump_dict = {

            }
    _dest_dict = {

            }
    
    def __init__(self):
        pass    

    def opcode(self, mnemonic):
        result = self._dest_dict.get(mnemonic)        
        if not result: 
            return None
        else: 
            return result


    def rs(self, mnemonic):
        if len(mnemonic) == 0:
            return None
        mnemonic = mnemonic.strip()
        print("comp find test::::", mnemonic)
        result = self._comp_dict.get(mnemonic)        
        if not result: 
            return None
        else: 
            return result

    def rt(self, mnemonic):
        mnemonic = mnemonic.strip()
        if len(mnemonic) == 0:
            return None
        result = self._jump_dict.get(mnemonic)        
        if not result: 
            return None
        else: 
            return result
    def rd(self, mnemonic): 
        pass 
    
    def shamt(self, mnemonic): 
        pass 
    
    def funct(self, mnemonic): 
        pass 
    
    def imm(self, mnemonic): 
        pass 
    
    def jAddr(self, mnemonic): 
        pass 
    
    
