# core/command_parser.py
def parse_command(cmd, swarm, roe, nuke_orb, dashboard):
    """
    Central command parser for CyberCrux OS simulation.
    """
    cmd = cmd.lower().strip()
    
    if any(keyword in cmd for keyword in ["falcon", "swarm", "launch swarm"]):
        return swarm.launch_swarm()
    
    elif any(keyword in cmd for keyword in ["nuke", "orb", "arm nuke"]):
        return nuke_orb.arm()
    
    elif "roe" in cmd or "rule" in cmd:
        return roe.status()
    
    elif "switch" in cmd:
        return f"✅ Dashboard switched to {dashboard} variant."
    
    elif "status" in cmd or "system" in cmd:
        integrity = getattr(swarm.kernel, 'integrity', 99.7)
        return (f"System Status:\n"
                f"• Kernel Integrity: {integrity}%\n"
                f"• Falcon Swarm: {'ACTIVE' if getattr(swarm, 'active', False) else 'STANDBY'}\n"
                f"• Nuke Orb: {nuke_orb.mode}")
    
    elif "help" in cmd or "?" in cmd:
        return ("Available commands:\n"
                "• launch falcon swarm\n"
                "• arm nuke orb\n"
                "• roe status\n"
                "• system status\n"
                "• switch to usa / france / asia\n"
                "• help\n"
                "• exit")
    
    else:
        return ("❌ Command not recognized.\n"
                "Try: 'launch falcon swarm', 'arm nuke orb', 'roe status', "
                "'system status', 'help'")
